<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:43:24.862192",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Ulam Spiral",
    "Prime Number Distribution",
    "Computer Vision",
    "Strong and Weak Primes"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Ulam Spiral": 0.78,
    "Prime Number Distribution": 0.77,
    "Computer Vision": 0.72,
    "Strong and Weak Primes": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is central to the paper's methodology and connects to a wide range of technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Ulam spiral",
        "canonical": "Ulam Spiral",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The Ulam Spiral is a unique concept in the paper, crucial for understanding the spatial distribution of primes.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "prime number distribution",
        "canonical": "Prime Number Distribution",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Prime Number Distribution is a key topic in number theory, relevant for linking to mathematical discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "image-focused machine learning model",
        "canonical": "Computer Vision",
        "aliases": [
          "image-based ML model"
        ],
        "category": "broad_technical",
        "rationale": "This links the paper's approach to the broader field of Computer Vision, highlighting the interdisciplinary method.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "strong and weak primes",
        "canonical": "Strong and Weak Primes",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Strong and Weak Primes are specific to the paper's cryptographic implications, offering unique technical insights.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "deterministic",
      "statistical behavior",
      "image-focused",
      "specific regions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Ulam spiral",
      "resolved_canonical": "Ulam Spiral",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "prime number distribution",
      "resolved_canonical": "Prime Number Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "image-focused machine learning model",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "strong and weak primes",
      "resolved_canonical": "Strong and Weak Primes",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Machine Learnability as a Measure of Order in Aperiodic Sequences

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18103.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18103](https://arxiv.org/abs/2509.18103)

## 🔗 유사한 논문
- [[2025-09-23/Causal Fuzzing for Verifying Machine Unlearning_20250923|Causal Fuzzing for Verifying Machine Unlearning]] (78.3% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (78.2% similar)
- [[2025-09-23/Elucidating the Design Space of FP4 training_20250923|Elucidating the Design Space of FP4 training]] (77.9% similar)
- [[2025-09-24/"What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts_20250924|"What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts]] (77.7% similar)
- [[2025-09-23/Random functions as data compressors for machine learning of molecular processes_20250923|Random functions as data compressors for machine learning of molecular processes]] (77.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]], [[keywords/Computer Vision|Computer Vision]]
**🔗 Specific Connectable**: [[keywords/Prime Number Distribution|Prime Number Distribution]]
**⚡ Unique Technical**: [[keywords/Ulam Spiral|Ulam Spiral]], [[keywords/Strong and Weak Primes|Strong and Weak Primes]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18103v1 Announce Type: new 
Abstract: Research on the distribution of prime numbers has revealed a dual character: deterministic in definition yet exhibiting statistical behavior reminiscent of random processes. In this paper we show that it is possible to use an image-focused machine learning model to measure the comparative regularity of prime number fields at specific regions of an Ulam spiral. Specifically, we demonstrate that in pure accuracy terms, models trained on blocks extracted from regions of the spiral in the vicinity of 500m outperform models trained on blocks extracted from the region representing integers lower than 25m. This implies existence of more easily learnable order in the former region than in the latter. Moreover, a detailed breakdown of precision and recall scores seem to imply that the model is favouring a different approach to classification in different regions of the spiral, focusing more on identifying prime patterns at lower numbers and more on eliminating composites at higher numbers. This aligns with number theory conjectures suggesting that at higher orders of magnitude we should see diminishing noise in prime number distributions, with averages (density, AP equidistribution) coming to dominate, while local randomness regularises after scaling by log x. Taken together, these findings point toward an interesting possibility: that machine learning can serve as a new experimental instrument for number theory. Notably, the method shows potential 1 for investigating the patterns in strong and weak primes for cryptographic purposes.

## 📝 요약

이 논문은 소수의 분포가 결정론적 정의를 가지면서도 통계적 특성을 보인다는 점에 주목하여, 이미지 기반 머신러닝 모델을 활용해 Ulam 나선의 특정 영역에서 소수 필드의 규칙성을 측정하는 방법을 제안합니다. 연구 결과, 500m 근처 영역에서 추출한 블록으로 학습한 모델이 25m 이하 정수를 대표하는 영역에서 학습한 모델보다 더 높은 정확도를 보였습니다. 이는 전자의 영역이 더 쉽게 학습 가능한 질서를 가진다는 것을 의미합니다. 또한, 모델이 나선의 다른 영역에서 소수 패턴을 식별하거나 합성수를 제거하는 방식이 다르다는 점이 발견되었습니다. 이는 소수 분포에서 높은 차수에서는 평균적인 특성이 지배적이 되며, 국소적 무작위성이 정규화된다는 수론의 추측과 일치합니다. 이러한 결과는 머신러닝이 수론 연구의 새로운 실험 도구로 활용될 가능성을 시사하며, 특히 강한 소수와 약한 소수의 패턴을 암호학적 목적으로 조사하는 데 유용할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 소수의 분포는 정의상 결정적이지만 통계적으로는 무작위 과정과 유사한 행동을 보인다.
- 2. Ulam 나선의 특정 영역에서 소수 필드의 규칙성을 이미지 기반 머신러닝 모델로 측정할 수 있다.
- 3. 500m 부근의 나선 영역에서 추출한 블록으로 학습한 모델이 25m 이하의 정수를 나타내는 영역에서 추출한 블록으로 학습한 모델보다 더 높은 정확도를 보인다.
- 4. 모델은 나선의 다른 영역에서 서로 다른 분류 접근 방식을 선호하며, 낮은 숫자에서는 소수 패턴 식별에, 높은 숫자에서는 합성수 제거에 중점을 둔다.
- 5. 머신러닝은 수론을 위한 새로운 실험 도구로 활용될 가능성이 있으며, 특히 강한 소수와 약한 소수의 패턴을 암호학적 목적으로 조사하는 데 잠재력을 보인다.


---

*Generated on 2025-09-24 14:43:24*