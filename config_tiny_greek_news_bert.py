# configuration_tiny_greek_news_bert.py
from transformers import BertConfig

class TinyGreekNewsBertConfig(BertConfig):
    """
    A thin wrapper around :class:`~transformers.BertConfig` that
    adds the extra hyper-parameters your model needs.
    """
    model_type = "tiny_greek_news_bert"      # appears in config.json

    def __init__(
        self,
        num_labels_class: int = 4,
        num_labels_ner:   int = 17,
        ner_loss_weight:  float = 3.0,
        **kwargs,
    ):
        super().__init__(**kwargs)

        # ---- extra fields used in TinyGreekNewsBert.forward() ----
        self.num_labels_class = num_labels_class
        self.num_labels_ner   = num_labels_ner
        self.ner_loss_weight  = ner_loss_weight


# ⚠️  This single call makes AutoConfig → TinyGreekNewsBertConfig
#     appear in the `auto_map` section of config.json
TinyGreekNewsBertConfig.register_for_auto_class()
