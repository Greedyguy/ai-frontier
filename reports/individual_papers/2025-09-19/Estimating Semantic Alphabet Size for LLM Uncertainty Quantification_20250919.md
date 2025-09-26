---
keywords:
  - Large Language Models
  - Semantic Entropy
  - Uncertainty Quantification
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14478
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:45:55.770785",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Semantic Entropy",
    "Uncertainty Quantification"
  ],
  "rejected_keywords": [
    "Hallucination Detection"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Semantic Entropy": 0.77,
    "Uncertainty Quantification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Estimating Semantic Alphabet Size for LLM Uncertainty Quantification

**Korean Title:** 대형 언어 모델의 불확실성 정량화를 위한 의미적 알파벳 크기 추정

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]], [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**⚡ Unique Technical**: [[keywords/Semantic Entropy|Semantic Entropy]]

## 🔗 유사한 논문
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (81.3% similar)
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (80.4% similar)
- [[Language Models Identify Ambiguities and Exploit Loopholes]] (80.3% similar)
- [[The Art of Saying Maybe A Conformal Lens for Uncertainty Benchmarking in VLMs]] (79.9% similar)
- [[Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14478v1 Announce Type: cross 
Abstract: Many black-box techniques for quantifying the uncertainty of large language models (LLMs) rely on repeated LLM sampling, which can be computationally expensive. Therefore, practical applicability demands reliable estimation from few samples. Semantic entropy (SE) is a popular sample-based uncertainty estimator with a discrete formulation attractive for the black-box setting. Recent extensions of semantic entropy exhibit improved LLM hallucination detection, but do so with less interpretable methods that admit additional hyperparameters. For this reason, we revisit the canonical discrete semantic entropy estimator, finding that it underestimates the "true" semantic entropy, as expected from theory. We propose a modified semantic alphabet size estimator, and illustrate that using it to adjust discrete semantic entropy for sample coverage results in more accurate semantic entropy estimation in our setting of interest. Furthermore, our proposed alphabet size estimator flags incorrect LLM responses as well or better than recent top-performing approaches, with the added benefit of remaining highly interpretable.

## 🔍 Abstract (한글 번역)

arXiv:2509.14478v1 발표 유형: 교차  
초록: 대형 언어 모델(LLMs)의 불확실성을 정량화하기 위한 많은 블랙박스 기법들은 반복적인 LLM 샘플링에 의존하며, 이는 계산적으로 비용이 많이 들 수 있습니다. 따라서 실용적인 적용 가능성은 적은 샘플로부터의 신뢰할 수 있는 추정을 요구합니다. 의미 엔트로피(SE)는 블랙박스 설정에 매력적인 이산적 공식으로, 샘플 기반 불확실성 추정기로 인기가 있습니다. 의미 엔트로피의 최근 확장은 LLM 환각 탐지를 개선하지만, 추가적인 하이퍼파라미터를 허용하는 덜 해석 가능한 방법을 사용합니다. 이러한 이유로, 우리는 정통적인 이산 의미 엔트로피 추정기를 재검토하여 이론적으로 예상되는 대로 "진정한" 의미 엔트로피를 과소평가한다는 것을 발견했습니다. 우리는 수정된 의미 알파벳 크기 추정기를 제안하며, 이를 샘플 커버리지에 맞춰 이산 의미 엔트로피를 조정하는 데 사용하면 우리의 관심 설정에서 더 정확한 의미 엔트로피 추정이 가능하다는 것을 보여줍니다. 더욱이, 제안된 알파벳 크기 추정기는 최근 최고 성능 접근법보다 잘못된 LLM 응답을 잘 또는 더 잘 표시하며, 높은 해석 가능성을 유지하는 추가적인 이점을 제공합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 불확실성을 정량화하는 데 있어 반복 샘플링을 필요로 하는 기존 방법의 계산 비용 문제를 해결하고자 합니다. 저자들은 샘플 기반 불확실성 추정기인 의미 엔트로피(SE)의 개선된 버전을 제안합니다. 기존의 SE는 "진정한" 의미 엔트로피를 과소평가하는 경향이 있어, 이를 보완하기 위해 수정된 의미 알파벳 크기 추정기를 도입했습니다. 이 새로운 추정기를 사용하면 샘플 커버리지를 조정하여 의미 엔트로피를 더 정확하게 추정할 수 있으며, LLM의 잘못된 응답을 효과적으로 식별할 수 있습니다. 제안된 방법은 해석 가능성을 유지하면서도 최신 기법들보다 성능이 우수합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 불확실성을 정량화하기 위한 많은 블랙박스 기법은 반복적인 LLM 샘플링에 의존하며, 이는 계산 비용이 많이 든다.

- 2. 기존의 이산적 의미 엔트로피 추정기는 "진정한" 의미 엔트로피를 과소평가하는 경향이 있다.

- 3. 제안된 수정된 의미 알파벳 크기 추정기를 사용하여 샘플 커버리지를 조정하면 더 정확한 의미 엔트로피 추정이 가능하다.

- 4. 제안된 알파벳 크기 추정기는 최근의 최상위 성능 접근법보다 더 해석 가능하면서도 LLM의 잘못된 응답을 효과적으로 식별한다.

---

*Generated on 2025-09-19 15:35:20*