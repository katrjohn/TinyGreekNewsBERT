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


# Model Description
This model is a distilled and finetuned version of [GreekBert](https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1)

## Dataset
The model was distilled and finetuned on the GreekNewsNERClassif [dataset](https://huggingface.co/datasets/katrjohn/Greek-News-NER-Classif)

### To use this model 
```
pip install transformers, torch
```

```
from transformers import AutoModel

model = AutoModel.from_pretrained("katrjohn/TinyGreekNewsBERT", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("nlpaueb/bert-base-greek-uncased-v1")
```

#### Example usage 
```
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("nlpaueb/bert-base-greek-uncased-v1")
model = AutoModel.from_pretrained("katrjohn/TinyGreekNewsBERT", trust_remote_code=True)

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

If you use the model, please cite the following:
```
@inproceedings{XXX,
author = {XXX},
title = {XXX},
year = {XXX},
isbn = {XXX},
publisher = {XXX},
address = {XXX},
url = {XXX},
booktitle = {XXX},
pages = {XXX},
numpages = {XXX},
location = {XXX},
series = {XXX}
}
```