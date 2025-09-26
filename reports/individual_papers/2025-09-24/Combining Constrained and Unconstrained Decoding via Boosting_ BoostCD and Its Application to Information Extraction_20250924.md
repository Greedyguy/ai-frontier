<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:53:14.942197",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Boosted Constrained Decoding",
    "Information Extraction",
    "Autoregressive Language Model",
    "Constrained Decoding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Boosted Constrained Decoding": 0.8,
    "Information Extraction": 0.85,
    "Autoregressive Language Model": 0.78,
    "Constrained Decoding": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Boosted Constrained Decoding",
        "canonical": "Boosted Constrained Decoding",
        "aliases": [
          "BoostCD"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, crucial for linking to specific applications in information extraction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Information Extraction",
        "canonical": "Information Extraction",
        "aliases": [
          "IE"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area for the proposed method, linking to broader NLP tasks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "Autoregressive Language Model",
        "canonical": "Autoregressive Language Model",
        "aliases": [
          "AR Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the method's operation, it connects to the broader field of language modeling.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Constrained Decoding",
        "canonical": "Constrained Decoding",
        "aliases": [
          "CD"
        ],
        "category": "specific_connectable",
        "rationale": "A critical component of the method, relevant for linking to structured prediction tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Boosted Constrained Decoding",
      "resolved_canonical": "Boosted Constrained Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Information Extraction",
      "resolved_canonical": "Information Extraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Autoregressive Language Model",
      "resolved_canonical": "Autoregressive Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Constrained Decoding",
      "resolved_canonical": "Constrained Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.14901.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2506.14901](https://arxiv.org/abs/2506.14901)

## 🔗 유사한 논문
- [[2025-09-24/Trace Is In Sentences_ Unbiased Lightweight ChatGPT-Generated Text Detector_20250924|Trace Is In Sentences: Unbiased Lightweight ChatGPT-Generated Text Detector]] (80.2% similar)
- [[2025-09-24/Align Where the Words Look_ Cross-Attention-Guided Patch Alignment with Contrastive and Transport Regularization for Bengali Captioning_20250924|Align Where the Words Look: Cross-Attention-Guided Patch Alignment with Contrastive and Transport Regularization for Bengali Captioning]] (80.2% similar)
- [[2025-09-23/Retrieval Enhanced Feedback via In-context Neural Error-book_20250923|Retrieval Enhanced Feedback via In-context Neural Error-book]] (79.9% similar)
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD: A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (79.9% similar)
- [[2025-09-23/PruneCD_ Contrasting Pruned Self Model to Improve Decoding Factuality_20250923|PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Autoregressive Language Model|Autoregressive Language Model]]
**🔗 Specific Connectable**: [[keywords/Information Extraction|Information Extraction]], [[keywords/Constrained Decoding|Constrained Decoding]]
**⚡ Unique Technical**: [[keywords/Boosted Constrained Decoding|Boosted Constrained Decoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.14901v2 Announce Type: replace 
Abstract: Many recent approaches to structured NLP tasks use an autoregressive language model $M$ to map unstructured input text $x$ to output text $y$ representing structured objects (such as tuples, lists, trees, code, etc.), where the desired output structure is enforced via constrained decoding. During training, these approaches do not require the model to be aware of the constraints, which are merely implicit in the training outputs $y$. This is advantageous as it allows for dynamic constraints without requiring retraining, but can lead to low-quality output during constrained decoding at test time. We overcome this problem with Boosted Constrained Decoding (BoostCD), which combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model $M$ twice, in constrained and unconstrained mode, obtaining two weak predictions. In phase 2, a learned autoregressive boosted model combines the two weak predictions into one final prediction. The mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance. We demonstrate the power of BoostCD by applying it to closed information extraction. Our model, BoostIE, outperforms prior approaches both in and out of distribution, addressing several common errors identified in those approaches.

## 📝 요약

이 논문은 구조화된 자연어 처리 작업에서 비구조화된 입력 텍스트를 구조화된 출력 텍스트로 변환하는 과정에서 발생하는 문제를 해결하기 위해 Boosted Constrained Decoding (BoostCD) 방법을 제안합니다. 기존 방법들은 제약 조건을 암묵적으로 학습하여 테스트 시 저품질 출력을 초래할 수 있었습니다. BoostCD는 제약된 디코딩과 비제약 디코딩을 결합하여 두 단계로 진행됩니다. 첫 번째 단계에서는 기본 모델이 제약된 모드와 비제약 모드로 두 가지 예측을 생성하고, 두 번째 단계에서는 학습된 모델이 이를 결합하여 최종 예측을 만듭니다. 이 방법은 상호 보완적인 오류를 활용하여 성능을 향상시킵니다. BoostCD는 정보 추출 작업에 적용되어 기존 방법보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 구조화된 NLP 작업을 위해 자가회귀 언어 모델을 사용하여 비구조화된 입력 텍스트를 구조화된 객체로 변환하는 방법이 최근 주목받고 있습니다.
- 2. 훈련 시 모델이 제약 조건을 인식할 필요가 없다는 점은 동적 제약 조건을 허용하지만, 테스트 시 제약된 디코딩에서 저품질의 출력을 초래할 수 있습니다.
- 3. Boosted Constrained Decoding (BoostCD)은 제약된 디코딩과 비제약 디코딩을 결합하여 두 단계로 문제를 해결합니다.
- 4. BoostCD의 첫 번째 단계에서는 기본 모델에서 제약된 모드와 비제약 모드로 두 가지 약한 예측을 생성하고, 두 번째 단계에서는 학습된 자가회귀 부스팅 모델이 두 예측을 결합하여 최종 예측을 만듭니다.
- 5. BoostCD를 폐쇄 정보 추출에 적용한 결과, BoostIE 모델이 기존 방법보다 더 나은 성능을 보이며 여러 일반적인 오류를 해결했습니다.


---

*Generated on 2025-09-24 15:53:14*