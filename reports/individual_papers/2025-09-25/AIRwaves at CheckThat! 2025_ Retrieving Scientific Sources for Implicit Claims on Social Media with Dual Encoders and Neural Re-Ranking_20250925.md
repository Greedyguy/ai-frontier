---
keywords:
  - Dual Encoder
  - Neural Re-Ranking
  - Dense Retrieval
  - Evidence Retrieval
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19509
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:37:27.061763",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dual Encoder",
    "Neural Re-Ranking",
    "Dense Retrieval",
    "Evidence Retrieval"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dual Encoder": 0.78,
    "Neural Re-Ranking": 0.82,
    "Dense Retrieval": 0.8,
    "Evidence Retrieval": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dual Encoder",
        "canonical": "Dual Encoder",
        "aliases": [
          "E5-large Encoder"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the retrieval pipeline and offers a unique approach to encoding for evidence retrieval.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Neural Re-Ranking",
        "canonical": "Neural Re-Ranking",
        "aliases": [
          "Re-Ranking",
          "SciBERT Re-Ranking"
        ],
        "category": "specific_connectable",
        "rationale": "This method enhances retrieval accuracy and is a key component of modern retrieval systems.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Dense Retrieval",
        "canonical": "Dense Retrieval",
        "aliases": [
          "Dense Vector Retrieval"
        ],
        "category": "specific_connectable",
        "rationale": "Dense retrieval is a modern approach that improves over traditional lexical methods, crucial for linking claims to sources.",
        "novelty_score": 0.58,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Evidence Retrieval",
        "canonical": "Evidence Retrieval",
        "aliases": [
          "Evidence-Based Retrieval"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept for fact-checking and linking claims to scientific sources.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "CheckThat!",
      "CLEF-2025"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dual Encoder",
      "resolved_canonical": "Dual Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Neural Re-Ranking",
      "resolved_canonical": "Neural Re-Ranking",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Dense Retrieval",
      "resolved_canonical": "Dense Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Evidence Retrieval",
      "resolved_canonical": "Evidence Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# AIRwaves at CheckThat! 2025: Retrieving Scientific Sources for Implicit Claims on Social Media with Dual Encoders and Neural Re-Ranking

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19509.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19509](https://arxiv.org/abs/2509.19509)

## 🔗 유사한 논문
- [[2025-09-22/RAVE_ Retrieval and Scoring Aware Verifiable Claim Detection_20250922|RAVE: Retrieval and Scoring Aware Verifiable Claim Detection]] (83.5% similar)
- [[2025-09-17/Combating Biomedical Misinformation through Multi-modal Claim Detection and Evidence-based Verification_20250917|Combating Biomedical Misinformation through Multi-modal Claim Detection and Evidence-based Verification]] (81.9% similar)
- [[2025-09-23/Multilingual vs Crosslingual Retrieval of Fact-Checked Claims_ A Tale of Two Approaches_20250923|Multilingual vs Crosslingual Retrieval of Fact-Checked Claims: A Tale of Two Approaches]] (81.9% similar)
- [[2025-09-17/Combining Evidence and Reasoning for Biomedical Fact-Checking_20250917|Combining Evidence and Reasoning for Biomedical Fact-Checking]] (81.6% similar)
- [[2025-09-23/Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning_20250923|Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Evidence Retrieval|Evidence Retrieval]]
**🔗 Specific Connectable**: [[keywords/Neural Re-Ranking|Neural Re-Ranking]], [[keywords/Dense Retrieval|Dense Retrieval]]
**⚡ Unique Technical**: [[keywords/Dual Encoder|Dual Encoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19509v1 Announce Type: cross 
Abstract: Linking implicit scientific claims made on social media to their original publications is crucial for evidence-based fact-checking and scholarly discourse, yet it is hindered by lexical sparsity, very short queries, and domain-specific language. Team AIRwaves ranked second in Subtask 4b of the CLEF-2025 CheckThat! Lab with an evidence-retrieval approach that markedly outperforms the competition baseline. The optimized sparse-retrieval baseline(BM25) achieves MRR@5 = 0.5025 on the gold label blind test set. To surpass this baseline, a two-stage retrieval pipeline is introduced: (i) a first stage that uses a dual encoder based on E5-large, fine-tuned using in-batch and mined hard negatives and enhanced through chunked tokenization and rich document metadata; and (ii) a neural re-ranking stage using a SciBERT cross-encoder. Replacing purely lexical matching with neural representations lifts performance to MRR@5 = 0.6174, and the complete pipeline further improves to MRR@5 = 0.6828. The findings demonstrate that coupling dense retrieval with neural re-rankers delivers a powerful and efficient solution for tweet-to-study matching and provides a practical blueprint for future evidence-retrieval pipelines.

## 📝 요약

이 논문은 소셜 미디어에서 암묵적으로 제기된 과학적 주장들을 원래의 학술 출판물과 연결하는 방법을 제안합니다. Team AIRwaves는 CLEF-2025 CheckThat! Lab의 Subtask 4b에서 두 번째로 높은 성과를 기록했습니다. 기본 BM25 모델을 개선하여 MRR@5 = 0.5025를 달성했으며, 이를 넘어서기 위해 두 단계의 검색 파이프라인을 도입했습니다. 첫 번째 단계는 E5-large 듀얼 인코더를 사용하고, 두 번째 단계는 SciBERT 크로스 인코더를 활용한 신경 재순위화 과정을 포함합니다. 이 방법은 MRR@5 = 0.6828로 성능을 향상시켰으며, 밀집 검색과 신경 재순위화의 결합이 효과적인 트윗-연구 매칭 솔루션을 제공함을 보여줍니다.

## 🎯 주요 포인트

- 1. 소셜 미디어에서의 암묵적 과학적 주장과 원본 출판물을 연결하는 것은 증거 기반 사실 확인과 학문적 담론에 필수적이다.
- 2. Team AIRwaves는 CLEF-2025 CheckThat! Lab의 Subtask 4b에서 두 번째로 높은 성과를 기록했다.
- 3. 두 단계의 검색 파이프라인을 도입하여 성능을 향상시켰으며, 이는 E5-large 기반의 듀얼 인코더와 SciBERT 크로스 인코더를 사용한다.
- 4. 순수한 어휘 매칭을 신경망 표현으로 대체하여 MRR@5 성능을 0.6828까지 끌어올렸다.
- 5. 연구 결과는 밀집 검색과 신경망 재순위화를 결합하여 트윗과 연구 간의 매칭에 강력하고 효율적인 솔루션을 제공함을 보여준다.


---

*Generated on 2025-09-25 15:37:27*