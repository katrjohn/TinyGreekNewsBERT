import torch.nn as nn
from transformers import BertModel, BertPreTrainedModel
from transformers import BertConfig, AutoTokenizer
from configuration_tiny_greek_news_bert import TinyGreekNewsBertConfig

class TinyGreekNewsBert(BertPreTrainedModel):
    config_class = TinyGreekNewsBertConfig
    def __init__(self, config):
        super().__init__(config)
        
        num_labels_class = config.num_labels_class
        num_labels_ner = config.num_labels_ner
        self.ner_loss_weight = getattr(config, "ner_loss_weight", 3.0)
        self.bert = BertModel(config)
        
        # Classification head
        self.class_dropout = nn.Dropout(0.3)
        self.class_fc = nn.Linear(config.hidden_size, 768)
        self.class_relu = nn.ReLU()
        self.classifier = nn.Linear(768, num_labels_class)
        
        # NER head
        self.ner_classifier = nn.Linear(config.hidden_size, num_labels_ner)
        
        self.init_weights()
        # For normalization
        self.initial_cls_loss = None
        self.initial_ner_loss = None
    def forward(self, input_ids, attention_mask=None, token_type_ids=None,
                labels_class=None, labels_ner=None):
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids
        )
        sequence_output = outputs.last_hidden_state   # (batch_size, seq_length, hidden_size)
        pooled_output = outputs.pooler_output           # (batch_size, hidden_size)
        
        # Classification branch
        pooled_output = self.class_dropout(pooled_output)
        x = self.class_fc(pooled_output)
        x = self.class_relu(x)
        logits_class = self.classifier(x)
        
        # NER branch
        logits_ner = self.ner_classifier(sequence_output)  # (batch_size, seq_length, num_labels_ner)
        
        loss = None
        if labels_class is not None and labels_ner is not None:
            # Classification loss
            loss_fct_class = nn.CrossEntropyLoss()
            loss_class = loss_fct_class(logits_class, labels_class)
            
            # NER loss: Cross-entropy with ignore_index=-100, summed then averaged over non-pad tokens
            loss_fct_ner = nn.CrossEntropyLoss(ignore_index=-100, reduction='sum')
            ner_loss_sum = loss_fct_ner(
                logits_ner.view(-1, logits_ner.shape[-1]), 
                labels_ner.view(-1)
            )
            mask = (labels_ner != -100).view(-1).float()
            loss_ner = ner_loss_sum / (mask.sum() + 1e-9)
            
            # Store initial values
            if self.initial_cls_loss is None and self.training:
                self.initial_cls_loss = loss_class.item()
            if self.initial_ner_loss is None and self.training:
                self.initial_ner_loss = loss_ner.item()
            
            # Normalize losses
            if (self.initial_cls_loss is not None) and (self.initial_ner_loss is not None):
                norm_cls_loss = loss_class / (self.initial_cls_loss + 1e-8)
                norm_ner_loss = loss_ner / (self.initial_ner_loss + 1e-8)
            else:
                norm_cls_loss = loss_class
                norm_ner_loss = loss_ner
            
            # Combine losses with weight
            loss = norm_cls_loss + self.ner_loss_weight * norm_ner_loss
            return (loss, logits_class, logits_ner)
        else:
            return (logits_class, logits_ner)
TinyGreekNewsBert.register_for_auto_class("AutoModel")
