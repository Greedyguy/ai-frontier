---
keywords:
  - Random Matrix Theory
  - Knowledge Distillation
  - Self-supervised Learning
  - Large Language Model
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15724
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:32:26.604306",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Random Matrix Theory",
    "Knowledge Distillation",
    "Self-supervised Learning",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Random Matrix Theory": 0.78,
    "Knowledge Distillation": 0.82,
    "Self-supervised Learning": 0.75,
    "Large Language Model": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Random Matrix Theory",
        "canonical": "Random Matrix Theory",
        "aliases": [
          "RMT"
        ],
        "category": "unique_technical",
        "rationale": "Random Matrix Theory is central to the paper's proposed method and offers a unique perspective on knowledge distillation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Knowledge Distillation",
        "canonical": "Knowledge Distillation",
        "aliases": [
          "KD"
        ],
        "category": "specific_connectable",
        "rationale": "Knowledge Distillation is a key process in the paper, linking it to broader machine learning compression techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Self-distillation",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-distillation"
        ],
        "category": "specific_connectable",
        "rationale": "Self-distillation is a form of self-supervised learning, enhancing the model's efficiency and stability.",
        "novelty_score": 0.6,
        "connectivity_score": 0.77,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      },
      {
        "surface": "Large Deep Learning Models",
        "canonical": "Large Language Model",
        "aliases": [
          "large models",
          "deep models"
        ],
        "category": "broad_technical",
        "rationale": "The paper addresses the challenges of deploying large models, a common issue in the field.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "compression method",
      "parameter reduction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Random Matrix Theory",
      "resolved_canonical": "Random Matrix Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Knowledge Distillation",
      "resolved_canonical": "Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Self-distillation",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.77,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Large Deep Learning Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation

**Korean Title:** RMT-KD: 랜덤 행렬 이론적 인과 지식 증류

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15724.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15724](https://arxiv.org/abs/2509.15724)

## 🔗 유사한 논문
- [[2025-09-19/Delta Knowledge Distillation for Large Language Models_20250919|Delta Knowledge Distillation for Large Language Models]] (83.4% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (81.4% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (81.1% similar)
- [[2025-09-22/Efficient Multimodal Dataset Distillation via Generative Models_20250922|Efficient Multimodal Dataset Distillation via Generative Models]] (80.6% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Knowledge Distillation|Knowledge Distillation]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Random Matrix Theory|Random Matrix Theory]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15724v1 Announce Type: new 
Abstract: Large deep learning models such as BERT and ResNet achieve state-of-the-art performance but are costly to deploy at the edge due to their size and compute demands. We present RMT-KD, a compression method that leverages Random Matrix Theory (RMT) for knowledge distillation to iteratively reduce network size. Instead of pruning or heuristic rank selection, RMT-KD preserves only informative directions identified via the spectral properties of hidden representations. RMT-based causal reduction is applied layer by layer with self-distillation to maintain stability and accuracy. On GLUE, AG News, and CIFAR-10, RMT-KD achieves up to 80% parameter reduction with only 2% accuracy loss, delivering 2.8x faster inference and nearly halved power consumption. These results establish RMT-KD as a mathematically grounded approach to network distillation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15724v1 발표 유형: 신규  
초록: BERT와 ResNet과 같은 대형 딥러닝 모델은 최첨단 성능을 달성하지만, 그 크기와 연산 요구 때문에 엣지에서의 배포가 비용이 많이 듭니다. 우리는 RMT-KD라는 압축 방법을 제시하며, 이는 랜덤 행렬 이론(RMT)을 활용한 지식 증류를 통해 네트워크 크기를 반복적으로 줄입니다. 가지치기나 휴리스틱 순위 선택 대신, RMT-KD는 숨겨진 표현의 스펙트럼 특성에 의해 식별된 정보 방향만을 보존합니다. RMT 기반의 인과적 축소는 안정성과 정확성을 유지하기 위해 자기 증류와 함께 층별로 적용됩니다. GLUE, AG News, CIFAR-10에서 RMT-KD는 최대 80%의 매개변수 감소와 단 2%의 정확도 손실로 2.8배 빠른 추론과 거의 절반의 전력 소비를 달성합니다. 이러한 결과는 RMT-KD를 네트워크 증류에 대한 수학적으로 근거 있는 접근 방식으로 확립합니다.

## 📝 요약

RMT-KD는 대형 딥러닝 모델의 크기와 연산 요구를 줄이기 위한 압축 방법으로, 랜덤 행렬 이론(RMT)을 활용한 지식 증류 기법입니다. 이 방법은 가지치기나 직관적 순위 선택 대신, 숨겨진 표현의 스펙트럼 특성을 통해 유용한 방향만을 보존합니다. 각 층에 RMT 기반 인과 감소를 적용하고, 자기 증류를 통해 안정성과 정확성을 유지합니다. GLUE, AG News, CIFAR-10 데이터셋에서 최대 80%의 매개변수 감소와 2%의 정확도 손실로, 2.8배 빠른 추론과 절반 수준의 전력 소모를 달성했습니다. RMT-KD는 수학적으로 근거 있는 네트워크 증류 접근법으로 자리 잡았습니다.

## 🎯 주요 포인트

- 1. RMT-KD는 랜덤 행렬 이론을 활용한 지식 증류 방법으로, 네트워크 크기를 반복적으로 줄입니다.
- 2. RMT-KD는 은닉 표현의 스펙트럼 특성을 통해 정보가 있는 방향만을 보존합니다.
- 3. GLUE, AG News, CIFAR-10 데이터셋에서 최대 80%의 파라미터 감소와 2%의 정확도 손실만으로 성능을 유지합니다.
- 4. RMT-KD는 추론 속도를 2.8배 향상시키고 전력 소비를 절반으로 줄입니다.
- 5. RMT-KD는 수학적으로 근거 있는 네트워크 증류 접근법으로 자리 잡았습니다.


---

*Generated on 2025-09-23 10:32:26*