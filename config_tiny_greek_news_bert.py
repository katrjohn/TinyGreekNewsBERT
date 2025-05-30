# configuration_tiny_greek_news_bert.py
from transformers import BertConfig

class TinyGreekNewsBertConfig(BertConfig):
    model_type = "tiny_greek_news_bert"
    def __init__(
        self,
        num_labels_class=19,
        num_labels_ner=32,
        ner_loss_weight=3.0,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.num_labels_class = num_labels_class
        self.num_labels_ner   = num_labels_ner
        self.ner_loss_weight  = ner_loss_weight

# 👇 this writes the AutoConfig mapping when you save_pretrained()
TinyGreekNewsBertConfig.register_for_auto_class()
