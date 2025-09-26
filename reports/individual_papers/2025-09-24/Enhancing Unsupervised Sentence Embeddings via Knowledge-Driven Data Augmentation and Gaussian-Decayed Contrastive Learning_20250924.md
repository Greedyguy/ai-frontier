<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:48:34.138189",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Knowledge Graphs",
    "Contrastive Sentence Embedding",
    "Semantic Textual Similarity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Knowledge Graphs": 0.82,
    "Contrastive Sentence Embedding": 0.78,
    "Semantic Textual Similarity": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the proposed method, linking to broader NLP advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Knowledge Graphs",
        "canonical": "Knowledge Graphs",
        "aliases": [
          "KG",
          "Knowledge Graph"
        ],
        "category": "specific_connectable",
        "rationale": "Knowledge Graphs are used to enhance data diversity, connecting to semantic data structuring.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Contrastive Sentence Embedding",
        "canonical": "Contrastive Sentence Embedding",
        "aliases": [
          "GCSE",
          "Gaussian-decayed Contrastive Sentence Embedding"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, crucial for understanding the proposed approach.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Semantic Textual Similarity",
        "canonical": "Semantic Textual Similarity",
        "aliases": [
          "STS"
        ],
        "category": "specific_connectable",
        "rationale": "STS tasks are a key application area for the proposed method, linking to evaluation metrics in NLP.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "data augmentation",
      "synthetic samples"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Knowledge Graphs",
      "resolved_canonical": "Knowledge Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Contrastive Sentence Embedding",
      "resolved_canonical": "Contrastive Sentence Embedding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Semantic Textual Similarity",
      "resolved_canonical": "Semantic Textual Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Enhancing Unsupervised Sentence Embeddings via Knowledge-Driven Data Augmentation and Gaussian-Decayed Contrastive Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2409.12887.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2409.12887](https://arxiv.org/abs/2409.12887)

## 🔗 유사한 논문
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.2% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (84.0% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.5% similar)
- [[2025-09-23/Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval_20250923|Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval]] (83.5% similar)
- [[2025-09-22/SEMMA_ A Semantic Aware Knowledge Graph Foundation Model_20250922|SEMMA: A Semantic Aware Knowledge Graph Foundation Model]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Knowledge Graphs|Knowledge Graphs]], [[keywords/Semantic Textual Similarity|Semantic Textual Similarity]]
**⚡ Unique Technical**: [[keywords/Contrastive Sentence Embedding|Contrastive Sentence Embedding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.12887v4 Announce Type: replace 
Abstract: Recently, using large language models (LLMs) for data augmentation has led to considerable improvements in unsupervised sentence embedding models. However, existing methods encounter two primary challenges: limited data diversity and high data noise. Current approaches often neglect fine-grained knowledge, such as entities and quantities, leading to insufficient diversity. Besides, unsupervised data frequently lacks discriminative information, and the generated synthetic samples may introduce noise. In this paper, we propose a pipeline-based data augmentation method via LLMs and introduce the Gaussian-decayed gradient-assisted Contrastive Sentence Embedding (GCSE) model to enhance unsupervised sentence embeddings. To tackle the issue of low data diversity, our pipeline utilizes knowledge graphs (KGs) to extract entities and quantities, enabling LLMs to generate more diverse samples. To address high data noise, the GCSE model uses a Gaussian-decayed function to limit the impact of false hard negative samples, enhancing the model's discriminative capability. Experimental results show that our approach achieves state-of-the-art performance in semantic textual similarity (STS) tasks, using fewer data samples and smaller LLMs, demonstrating its efficiency and robustness across various models.

## 📝 요약

최근 대형 언어 모델(LLM)을 활용한 데이터 증강이 비지도 문장 임베딩 모델의 성능을 크게 향상시켰습니다. 그러나 기존 방법은 데이터 다양성과 노이즈 문제를 겪고 있습니다. 본 논문에서는 LLM을 통한 파이프라인 기반 데이터 증강 방법과 가우시안 감쇠 기울기 보조 대조 문장 임베딩(GCSE) 모델을 제안합니다. 데이터 다양성을 높이기 위해 지식 그래프(KG)를 활용하여 엔티티와 수량을 추출하고, LLM이 더 다양한 샘플을 생성하도록 합니다. 또한, GCSE 모델은 가우시안 감쇠 함수를 사용해 잘못된 하드 네거티브 샘플의 영향을 줄여 모델의 변별력을 강화합니다. 실험 결과, 제안된 방법은 적은 데이터와 작은 LLM을 사용하면서도 의미적 텍스트 유사성(STS) 과제에서 최첨단 성능을 달성하여 효율성과 강건성을 입증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)을 활용한 데이터 증강이 비지도 문장 임베딩 모델의 성능을 크게 향상시켰습니다.
- 2. 기존 방법들은 데이터 다양성과 데이터 노이즈 문제를 겪고 있으며, 세밀한 지식(예: 엔티티, 수량)을 간과하여 다양성이 부족합니다.
- 3. 제안된 방법은 지식 그래프(KGs)를 활용하여 LLMs가 더 다양한 샘플을 생성하도록 하고, Gaussian-decayed 함수로 노이즈 문제를 해결합니다.
- 4. Gaussian-decayed gradient-assisted Contrastive Sentence Embedding (GCSE) 모델은 잘못된 하드 네거티브 샘플의 영향을 제한하여 모델의 판별 능력을 향상시킵니다.
- 5. 실험 결과, 제안된 방법은 적은 데이터 샘플과 더 작은 LLMs를 사용하여 의미적 텍스트 유사성(STS) 작업에서 최첨단 성능을 달성했습니다.


---

*Generated on 2025-09-24 15:48:34*