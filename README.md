---
license: mit
datasets:
- katrjohn/Greek-News-NER-Classif
language:
- el
base_model:
- nlpaueb/bert-base-greek-uncased-v1
tags:
- NewsArticle
- Classification
- NER
---




## $${\color{gold} \textsf{You can test a live version of the model here! https://huggingface.co/spaces/katrjohn/TinyGreekNewsBERT}}$$

# Model Description
This model is a 14.1M parameter distilled and finetuned version of [GreekBert](https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1)

## Dataset
The model was distilled and finetuned on the [GreekNews-20k](https://huggingface.co/datasets/katrjohn/GreekNews-20k) and [News Articles in Greek](https://www.kaggle.com/datasets/kpittos/news-articles) datasets.

### Results

Perfomance on the [GreekNews-20k dataset](https://huggingface.co/datasets/katrjohn/GreekNews-20k) :

| Class                                           | Precision | Recall | F1-score | Support |
|-------------------------------------------------|-----------|--------|----------|---------|
| Αυτοκίνητο                                      | 0.87      | 0.95   | 0.90     | 201     |
| Επιχειρήσεις και βιομηχανία                     | 0.68      | 0.76   | 0.72     | 369     |
| Έγκλημα και δικαιοσύνη                          | 0.86      | 0.87   | 0.87     | 314     |
| Ειδήσεις για καταστροφές και έκτακτες ανάγκες   | 0.79      | 0.71   | 0.75     | 272     |
| Οικονομικά και χρηματοοικονομικά                | 0.78      | 0.70   | 0.73     | 495     |
| Εκπαίδευση                                      | 0.86      | 0.83   | 0.84     | 259     |
| Ψυχαγωγία και πολιτισμός                        | 0.68      | 0.79   | 0.73     | 251     |
| Περιβάλλον και κλίμα                           | 0.78      | 0.65   | 0.71     | 292     |
| Οικογένεια και σχέσεις                          | 0.80      | 0.81   | 0.81     | 294     |
| Μόδα                                            | 0.84      | 0.91   | 0.87     | 259     |
| Τρόφιμα και ποτά                                | 0.65      | 0.75   | 0.70     | 262     |
| Υγεία και ιατρική                               | 0.74      | 0.64   | 0.68     | 346     |
| Μεταφορές και υποδομές                          | 0.78      | 0.82   | 0.80     | 321     |
| Ψυχική υγεία και ευεξία                         | 0.72      | 0.72   | 0.72     | 348     |
| Πολιτική και κυβέρνηση                          | 0.76      | 0.68   | 0.72     | 339     |
| Θρησκεία                                        | 0.92      | 0.87   | 0.90     | 271     |
| Αθλητισμός                                      | 0.97      | 0.98   | 0.97     | 212     |
| Ταξίδια και αναψυχή                             | 0.80      | 0.80   | 0.80     | 424     |
| Τεχνολογία και επιστήμη                         | 0.65      | 0.75   | 0.70     | 308     |
| **Accuracy**                                    |           |        | 0.78     | 5837    |
| **Macro avg**                                   | 0.79      | 0.79   | 0.79     | 5837    |
| **Weighted avg**                                | 0.78      | 0.78   | 0.78     | 5837    |

| Entity    | Precision | Recall | F1-score | Support |
|----------|-----------|--------|----------|---------|
| CARDINAL | 0.87      | 0.93   | 0.90     | 25656   |
| DATE     | 0.87      | 0.90   | 0.88     | 15469   |
| EVENT    | 0.60      | 0.59   | 0.59     | 1720    |
| FAC      | 0.39      | 0.51   | 0.44     | 2118    |
| GPE      | 0.88      | 0.86   | 0.87     | 16010   |
| LOC      | 0.72      | 0.65   | 0.68     | 3547    |
| MONEY    | 0.73      | 0.76   | 0.74     | 3882    |
| NORP     | 0.89      | 0.84   | 0.86     | 1926    |
| ORDINAL  | 0.92      | 0.96   | 0.94     | 3891    |
| ORG      | 0.69      | 0.76   | 0.72     | 22184   |
| PERCENT  | 0.72      | 0.78   | 0.75     | 7286    |
| PERSON   | 0.79      | 0.85   | 0.82     | 16524   |
| PRODUCT  | 0.48      | 0.48   | 0.48     | 2071    |
| QUANTITY | 0.64      | 0.68   | 0.66     | 2588    |
| TIME     | 0.74      | 0.76   | 0.75     | 2390    |
| **Micro avg** | 0.78  | 0.83   | 0.81     | 127262  |
| **Macro avg** | 0.73  | 0.75   | 0.74     | 127262  |
| **Weighted avg** | 0.79 | 0.83 | 0.81     | 127262  |

Performance on the [elNER dataset](https://github.com/nmpartzio/elNER) :

| Entity    | Precision | Recall | F1-score | Support |
|----------|-----------|--------|----------|---------|
| CARDINAL | 0.90      | 0.93   | 0.91     | 911     |
| DATE     | 0.90      | 0.92   | 0.91     | 838     |
| EVENT    | 0.43      | 0.46   | 0.45     | 130     |
| FAC      | 0.34      | 0.47   | 0.40     | 77      |
| GPE      | 0.83      | 0.90   | 0.86     | 826     |
| LOC      | 0.70      | 0.63   | 0.66     | 178     |
| MONEY    | 0.93      | 0.95   | 0.94     | 111     |
| NORP     | 0.81      | 0.87   | 0.84     | 141     |
| ORDINAL  | 0.94      | 0.92   | 0.93     | 172     |
| ORG      | 0.74      | 0.72   | 0.73     | 1388    |
| PERCENT  | 0.93      | 0.99   | 0.96     | 206     |
| PERSON   | 0.84      | 0.86   | 0.85     | 1051    |
| PRODUCT  | 0.46      | 0.41   | 0.43     | 83      |
| QUANTITY | 0.70      | 0.75   | 0.73     | 65      |
| TIME     | 0.88      | 0.81   | 0.84     | 137     |
| **Micro avg** | 0.82  | 0.83   | 0.82     | 6314    |
| **Macro avg** | 0.76  | 0.77   | 0.76     | 6314    |
| **Weighted avg** | 0.82 | 0.83 | 0.82     | 6314    |



#### To use this model 
```
pip install transformers, torch
```

```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("katrjohn/TinyGreekNewsBERT", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("nlpaueb/bert-base-greek-uncased-v1")
```

##### Example usage 
```python
import torch

# Classification label dictionary (reverse)
classification_label_dict_reverse = {
    0: "Αυτοκίνητο", 1: "Επιχειρήσεις και βιομηχανία", 2: "Έγκλημα και δικαιοσύνη",
    3: "Ειδήσεις για καταστροφές και έκτακτες ανάγκες", 4: "Οικονομικά και χρηματοοικονομικά", 5: "Εκπαίδευση",
    6: "Ψυχαγωγία και πολιτισμός", 7: "Περιβάλλον και κλίμα", 8: "Οικογένεια και σχέσεις",
    9: "Μόδα", 10: "Τρόφιμα και ποτά", 11: "Υγεία και ιατρική", 12: "Μεταφορές και υποδομές",
    13: "Ψυχική υγεία και ευεξία", 14: "Πολιτική και κυβέρνηση", 15: "Θρησκεία",
    16: "Αθλητισμός", 17: "Ταξίδια και αναψυχή", 18: "Τεχνολογία και επιστήμη"
}

ner_label_set = ["PAD", "O",
    "B-ORG", "I-ORG", "B-PERSON", "I-PERSON", "B-CARDINAL", "I-CARDINAL",
    "B-GPE", "I-GPE", "B-DATE", "I-DATE", "B-ORDINAL", "I-ORDINAL",
    "B-PERCENT", "I-PERCENT", "B-LOC", "I-LOC", "B-NORP", "I-NORP",
    "B-MONEY", "I-MONEY", "B-TIME", "I-TIME", "B-EVENT", "I-EVENT",
    "B-PRODUCT", "I-PRODUCT", "B-FAC", "I-FAC", "B-QUANTITY", "I-QUANTITY"
]
tag2idx = {t:i for i,t in enumerate(ner_label_set)}
idx2tag = {i:t for t,i in tag2idx.items()}

sentence = "Ο Κυριάκος Μητσοτάκης επισκέφθηκε τη Θεσσαλονίκη για τα εγκαίνια της ΔΕΘ."
inputs = tokenizer(sentence, return_tensors="pt")

with torch.no_grad():
    classification_logits, ner_logits = model(**inputs)

# Classification
classification_probs = torch.softmax(classification_logits, dim=-1)
predicted_class = torch.argmax(classification_probs, dim=-1).item()
predicted_class_label = classification_label_dict_reverse.get(predicted_class, "Unknown")

print(f"Predicted class index: {predicted_class}")
print(f"Predicted class label: {predicted_class_label}")

# NER
ner_predictions = torch.argmax(ner_logits, dim=-1).squeeze().tolist()
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze())

for token, pred_idx in zip(tokens, ner_predictions):
    tag = idx2tag.get(pred_idx, "O")
    if token in ["[CLS]", "[SEP]"]:
        tag = "O"
    print(f"{token}: {tag}")


```

Output:
```
Predicted class index: 14
Predicted class label: Πολιτική και κυβέρνηση
[CLS]: O
ο: O
κυριακος: B-PERSON
μητσοτακης: I-PERSON
επισκεφθηκε: O
τη: O
θεσσαλονικη: B-GPE
για: O
τα: O
εγκαινια: O
της: O
δεθ: B-EVENT
.: O
[SEP]: O

```

#### Author
This model has been released along side with the article: Named Entity Recognition and News Article Classification: A Lightweight Approach.
To use this model please cite the following:
```
@article{Katranis2025Access,
  author  = {Ioannis Katranis and Christos Troussas and Akrivi Krouska and Phivos Mylonas and Cleo Sgouropoulou},
  title   = {Named Entity Recognition and News Article Classification: A Lightweight Approach},
  journal = {IEEE Access},
  year    = {2025},
  pages   = {1--1},
  issn    = {2169-3536},
  doi     = {10.1109/ACCESS.2025.3605709},
  url     = {https://ieeexplore.ieee.org/document/11148234},
  note    = {Early Access},
  month   = sep
}

```
