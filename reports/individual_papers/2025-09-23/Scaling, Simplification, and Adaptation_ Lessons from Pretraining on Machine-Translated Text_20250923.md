---
keywords:
  - Multilingual Pretraining
  - Machine Translation
  - Source-side Simplification
  - Pretraining on MT-derived Data
  - Cultural Nuance Tasks
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17317
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:51:53.979505",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multilingual Pretraining",
    "Machine Translation",
    "Source-side Simplification",
    "Pretraining on MT-derived Data",
    "Cultural Nuance Tasks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multilingual Pretraining": 0.78,
    "Machine Translation": 0.8,
    "Source-side Simplification": 0.77,
    "Pretraining on MT-derived Data": 0.79,
    "Cultural Nuance Tasks": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multilingual Pretraining",
        "canonical": "Multilingual Pretraining",
        "aliases": [
          "Multilingual Training"
        ],
        "category": "unique_technical",
        "rationale": "This concept addresses the challenge of language imbalance in pretraining, which is central to the paper's investigation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Machine Translation",
        "canonical": "Machine Translation",
        "aliases": [
          "MT"
        ],
        "category": "broad_technical",
        "rationale": "Machine Translation is a core method used in the study to generate data for pretraining, linking it to broader NLP research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Source-side Simplification",
        "canonical": "Source-side Simplification",
        "aliases": [
          "Simplifying Source Text"
        ],
        "category": "unique_technical",
        "rationale": "This technique is explored as a potential method to improve model generalization, making it a unique focus of the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Pretraining on MT-derived Data",
        "canonical": "Pretraining on MT-derived Data",
        "aliases": [
          "MT Data Pretraining"
        ],
        "category": "unique_technical",
        "rationale": "The paper investigates the effectiveness of this pretraining strategy, which is crucial for understanding its findings.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.79
      },
      {
        "surface": "Cultural Nuance Tasks",
        "canonical": "Cultural Nuance Tasks",
        "aliases": [
          "Culturally Sensitive Tasks"
        ],
        "category": "unique_technical",
        "rationale": "These tasks highlight the limitations of MT-pretrained models, emphasizing the need for native data exposure.",
        "novelty_score": 0.66,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "data wall",
      "model capacity",
      "native text"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multilingual Pretraining",
      "resolved_canonical": "Multilingual Pretraining",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Machine Translation",
      "resolved_canonical": "Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Source-side Simplification",
      "resolved_canonical": "Source-side Simplification",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Pretraining on MT-derived Data",
      "resolved_canonical": "Pretraining on MT-derived Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.76,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Cultural Nuance Tasks",
      "resolved_canonical": "Cultural Nuance Tasks",
      "decision": "linked",
      "scores": {
        "novelty": 0.66,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Scaling, Simplification, and Adaptation: Lessons from Pretraining on Machine-Translated Text

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17317.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17317](https://arxiv.org/abs/2509.17317)

## 🔗 유사한 논문
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (85.6% similar)
- [[2025-09-22/Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation_20250922|Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation]] (84.3% similar)
- [[2025-09-22/The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation_20250922|The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation]] (83.8% similar)
- [[2025-09-23/Rethinking the Role of Text Complexity in Language Model Pretraining_20250923|Rethinking the Role of Text Complexity in Language Model Pretraining]] (83.2% similar)
- [[2025-09-19/Translate, then Detect_ Leveraging Machine Translation for Cross-Lingual Toxicity Classification_20250919|Translate, then Detect: Leveraging Machine Translation for Cross-Lingual Toxicity Classification]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Translation|Machine Translation]]
**⚡ Unique Technical**: [[keywords/Multilingual Pretraining|Multilingual Pretraining]], [[keywords/Source-side Simplification|Source-side Simplification]], [[keywords/Pretraining on MT-derived Data|Pretraining on MT-derived Data]], [[keywords/Cultural Nuance Tasks|Cultural Nuance Tasks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17317v1 Announce Type: cross 
Abstract: Most languages lack sufficient data for large-scale monolingual pretraining, creating a "data wall." Multilingual pretraining helps but is limited by language imbalance and the "curse of multilinguality." An alternative is to translate high-resource text with machine translation (MT), which raises three questions: (1) How does MT-derived data scale with model capacity? (2) Can source-side transformations (e.g., simplifying English with an LLM) improve generalization to native text? (3) How well do models pretrained on MT-derived data adapt when continually trained on limited native text? We investigate these questions by translating English into Indonesian and Tamil--two typologically distant, lower-resource languages--and pretraining GPT-2 models (124M-774M) on native or MT-derived corpora from raw and LLM-simplified English. We evaluate cross-entropy loss on native text, along with accuracy on syntactic probes and downstream tasks. Our results show that (1) MT-pretrained models benefit from scaling; (2) source-side simplification harms generalization to native text; and (3) adapting MT-pretrained models on native text often yields better performance than native-only models, even with less native data. However, tasks requiring cultural nuance (e.g., toxicity detection) demand more exposure to native data.

## 📝 요약

이 논문은 대규모 단일언어 사전학습에 필요한 데이터가 부족한 언어들을 대상으로, 기계 번역(MT)을 활용한 대안을 제시합니다. 연구는 영어를 인도네시아어와 타밀어로 번역하여 GPT-2 모델을 사전학습하고, 원어민 텍스트에 대한 일반화와 적응력을 평가합니다. 주요 발견사항은 다음과 같습니다: (1) MT로 사전학습한 모델은 규모가 커질수록 성능이 향상됩니다. (2) 원본 텍스트를 단순화하는 것은 원어민 텍스트에 대한 일반화에 부정적 영향을 미칩니다. (3) MT 데이터로 사전학습한 모델을 원어민 데이터로 추가 학습하면, 제한된 원어민 데이터만 사용한 모델보다 성능이 우수합니다. 그러나 문화적 뉘앙스를 요구하는 작업에는 더 많은 원어민 데이터가 필요합니다.

## 🎯 주요 포인트

- 1. 다국어 사전 학습은 언어 불균형과 다국어의 저주로 인해 한계가 있다.
- 2. 기계 번역을 통한 데이터는 모델 용량이 증가할수록 성능이 향상된다.
- 3. 원본 텍스트를 단순화하는 것은 원어 텍스트에 대한 일반화에 부정적인 영향을 미친다.
- 4. 기계 번역 데이터를 사전 학습한 모델은 제한된 원어 텍스트로 지속적으로 학습할 때 성능이 향상된다.
- 5. 문화적 뉘앙스가 필요한 작업에서는 더 많은 원어 데이터가 필요하다.


---

*Generated on 2025-09-23 23:51:53*