<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:44:00.455328",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Test-Time Scaling",
    "Machine Translation",
    "Neural MT Evaluation Metrics",
    "Compute Budget"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Test-Time Scaling": 0.78,
    "Machine Translation": 0.85,
    "Neural MT Evaluation Metrics": 0.7,
    "Compute Budget": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Test-Time Scaling",
        "canonical": "Test-Time Scaling",
        "aliases": [
          "TTS"
        ],
        "category": "unique_technical",
        "rationale": "Test-Time Scaling is a novel approach in the context of machine translation, offering a unique perspective on computational efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Machine Translation",
        "canonical": "Machine Translation",
        "aliases": [
          "MT"
        ],
        "category": "broad_technical",
        "rationale": "Machine Translation is a core area of study within NLP, providing a strong link to related research in language processing.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Neural MT Evaluation Metrics",
        "canonical": "Neural MT Evaluation Metrics",
        "aliases": [
          "neural machine translation metrics"
        ],
        "category": "specific_connectable",
        "rationale": "These metrics are crucial for assessing translation quality, linking to broader discussions on evaluation in NLP.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Compute Budget",
        "canonical": "Compute Budget",
        "aliases": [
          "computational budget"
        ],
        "category": "specific_connectable",
        "rationale": "Compute Budget is a key factor in model performance and efficiency, relevant to discussions on resource allocation in AI.",
        "novelty_score": 0.5,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "scaling",
      "model parameters",
      "language pairs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Test-Time Scaling",
      "resolved_canonical": "Test-Time Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Machine Translation",
      "resolved_canonical": "Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Neural MT Evaluation Metrics",
      "resolved_canonical": "Neural MT Evaluation Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Compute Budget",
      "resolved_canonical": "Compute Budget",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Investigating Test-Time Scaling with Reranking for Machine Translation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19020.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.19020](https://arxiv.org/abs/2509.19020)

## 🔗 유사한 논문
- [[2025-09-23/Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling_20250923|Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling]] (85.9% similar)
- [[2025-09-18/Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality_20250918|Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality]] (83.0% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (82.8% similar)
- [[2025-09-23/Transformer-Encoder Trees for Efficient Multilingual Machine Translation and Speech Translation_20250923|Transformer-Encoder Trees for Efficient Multilingual Machine Translation and Speech Translation]] (82.5% similar)
- [[2025-09-23/Scaling, Simplification, and Adaptation_ Lessons from Pretraining on Machine-Translated Text_20250923|Scaling, Simplification, and Adaptation: Lessons from Pretraining on Machine-Translated Text]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Translation|Machine Translation]]
**🔗 Specific Connectable**: [[keywords/Neural MT Evaluation Metrics|Neural MT Evaluation Metrics]], [[keywords/Compute Budget|Compute Budget]]
**⚡ Unique Technical**: [[keywords/Test-Time Scaling|Test-Time Scaling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19020v1 Announce Type: new 
Abstract: Scaling model parameters has become the de facto strategy for improving NLP systems, but it comes with substantial computational costs. Test-Time Scaling (TTS) offers an alternative by allocating more computation at inference: generating multiple candidates and selecting the best. While effective in tasks such as mathematical reasoning, TTS has not been systematically explored for machine translation (MT). In this paper, we present the first systematic study of TTS for MT, investigating a simple but practical best-of-N framework on WMT24 benchmarks. Our experiments cover six high-resource and one low-resource language pairs, five model sizes (3B-72B), and various TTS compute budget (N up to 1024). Our results show that a) For high-resource languages, TTS generally improves translation quality according to multiple neural MT evaluation metrics, and our human evaluation confirms these gains; b) Augmenting smaller models with large $N$ can match or surpass larger models at $N{=}1$ with more compute cost; c) Under fixed compute budgets, larger models are typically more efficient, and TTS can degrade quality due to metric blind spots in low-resource cases.

## 📝 요약

이 논문은 기계 번역(MT)에서 테스트 시 스케일링(TTS)의 체계적인 연구를 최초로 수행하였습니다. TTS는 추론 시 여러 후보를 생성하고 최적의 결과를 선택하여 번역 품질을 향상시키는 방법입니다. WMT24 벤치마크를 통해 고자원 및 저자원 언어 쌍을 대상으로 다양한 모델 크기(3B-72B)와 TTS 계산 예산(N 최대 1024)을 실험하였습니다. 주요 발견사항은 다음과 같습니다: a) 고자원 언어의 경우, TTS는 번역 품질을 개선하며 이는 인간 평가에서도 확인되었습니다. b) 작은 모델에 큰 N을 적용하면 더 큰 모델의 성능을 초과할 수 있습니다. c) 고정된 계산 예산 하에서는 큰 모델이 일반적으로 더 효율적이며, 저자원 언어의 경우 TTS가 품질을 저하시킬 수 있습니다.

## 🎯 주요 포인트

- 1. 테스트 타임 스케일링(TTS)은 NLP 시스템의 성능을 향상시키기 위한 대안으로, 추론 시 더 많은 계산을 할당하여 여러 후보를 생성하고 최적의 결과를 선택하는 방법이다.
- 2. 본 연구는 기계 번역(MT) 분야에서 TTS의 체계적인 첫 연구로, WMT24 벤치마크에서 단순하지만 실용적인 best-of-N 프레임워크를 조사하였다.
- 3. 실험 결과, 고자원 언어의 경우 TTS가 번역 품질을 향상시키며, 이는 여러 신경망 MT 평가 지표와 인간 평가에서도 확인되었다.
- 4. 작은 모델에 큰 N을 적용하면 더 많은 계산 비용을 들여 N=1의 큰 모델과 맞먹거나 이를 능가할 수 있다.
- 5. 고정된 계산 예산 하에서는 큰 모델이 일반적으로 더 효율적이며, 저자원 언어의 경우 TTS가 품질을 저하시킬 수 있다.


---

*Generated on 2025-09-24 15:44:00*