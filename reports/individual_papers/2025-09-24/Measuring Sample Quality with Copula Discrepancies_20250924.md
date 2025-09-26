<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:34:52.259732",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Copula Discrepancy",
    "Markov Chain Monte Carlo",
    "Stochastic Gradient Langevin Dynamics",
    "Sklar's Theorem"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Copula Discrepancy": 0.8,
    "Markov Chain Monte Carlo": 0.85,
    "Stochastic Gradient Langevin Dynamics": 0.78,
    "Sklar's Theorem": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Copula Discrepancy",
        "canonical": "Copula Discrepancy",
        "aliases": [
          "CD"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel diagnostic tool specifically designed for assessing dependence structures in biased MCMC samples.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Markov chain Monte Carlo",
        "canonical": "Markov Chain Monte Carlo",
        "aliases": [
          "MCMC"
        ],
        "category": "broad_technical",
        "rationale": "A foundational technique in Bayesian machine learning, relevant for connecting various sampling and inference methods.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Stochastic Gradient Langevin Dynamics",
        "canonical": "Stochastic Gradient Langevin Dynamics",
        "aliases": [
          "SGLD"
        ],
        "category": "specific_connectable",
        "rationale": "A specific MCMC variant that balances computational efficiency with sampling accuracy, relevant for discussions on biased samplers.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sklar's theorem",
        "canonical": "Sklar's Theorem",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Provides the theoretical foundation for separating dependence structures from marginal distributions in copulas.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "sample quality",
      "diagnostic gap",
      "traditional methods",
      "computational overhead"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Copula Discrepancy",
      "resolved_canonical": "Copula Discrepancy",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Markov chain Monte Carlo",
      "resolved_canonical": "Markov Chain Monte Carlo",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Stochastic Gradient Langevin Dynamics",
      "resolved_canonical": "Stochastic Gradient Langevin Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sklar's theorem",
      "resolved_canonical": "Sklar's Theorem",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Measuring Sample Quality with Copula Discrepancies

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.21434.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2507.21434](https://arxiv.org/abs/2507.21434)

## 🔗 유사한 논문
- [[2025-09-23/DISCO_ Mitigating Bias in Deep Learning with Conditional Distance Correlation_20250923|DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation]] (81.9% similar)
- [[2025-09-23/Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation_20250923|Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation]] (81.5% similar)
- [[2025-09-23/Parallel Simulation for Log-concave Sampling and Score-based Diffusion Models_20250923|Parallel Simulation for Log-concave Sampling and Score-based Diffusion Models]] (80.2% similar)
- [[2025-09-24/A Generalized Bisimulation Metric of State Similarity between Markov Decision Processes_ From Theoretical Propositions to Applications_20250924|A Generalized Bisimulation Metric of State Similarity between Markov Decision Processes: From Theoretical Propositions to Applications]] (80.0% similar)
- [[2025-09-23/DISCO_ Disentangled Communication Steering for Large Language Models_20250923|DISCO: Disentangled Communication Steering for Large Language Models]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Markov Chain Monte Carlo|Markov Chain Monte Carlo]]
**🔗 Specific Connectable**: [[keywords/Stochastic Gradient Langevin Dynamics|Stochastic Gradient Langevin Dynamics]]
**⚡ Unique Technical**: [[keywords/Copula Discrepancy|Copula Discrepancy]], [[keywords/Sklar's Theorem|Sklar's Theorem]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.21434v2 Announce Type: replace-cross 
Abstract: The scalable Markov chain Monte Carlo (MCMC) algorithms that underpin modern Bayesian machine learning, such as Stochastic Gradient Langevin Dynamics (SGLD), sacrifice asymptotic exactness for computational speed, creating a critical diagnostic gap: traditional sample quality measures fail catastrophically when applied to biased samplers. While powerful Stein-based diagnostics can detect distributional mismatches, they provide no direct assessment of dependence structure, often the primary inferential target in multivariate problems. We introduce the Copula Discrepancy (CD), a principled and computationally efficient diagnostic that leverages Sklar's theorem to isolate and quantify the fidelity of a sample's dependence structure independent of its marginals. Our theoretical framework provides the first structure-aware diagnostic specifically designed for the era of approximate inference. Empirically, we demonstrate that a moment-based CD dramatically outperforms standard diagnostics like effective sample size for hyperparameter selection in biased MCMC, correctly identifying optimal configurations where traditional methods fail. Furthermore, our robust MLE-based variant can detect subtle but critical mismatches in tail dependence that remain invisible to rank correlation-based approaches, distinguishing between samples with identical Kendall's tau but fundamentally different extreme-event behavior. With computational overhead orders of magnitude lower than existing Stein discrepancies, the CD provides both immediate practical value for MCMC practitioners and a theoretical foundation for the next generation of structure-aware sample quality assessment.

## 📝 요약

이 논문은 현대 베이지안 기계 학습에서 사용되는 확장 가능한 마르코프 체인 몬테카를로(MCMC) 알고리즘의 진단 문제를 해결하기 위해 새로운 방법론인 Copula Discrepancy (CD)를 제안합니다. 기존의 진단 방법들은 편향된 샘플러에 대해 효과적이지 않으며, 특히 다변량 문제에서 중요한 의존 구조를 평가하는 데 한계가 있습니다. CD는 Sklar의 정리를 활용하여 샘플의 의존 구조를 독립적으로 평가하며, 이론적 기반을 제공하여 근사 추론 시대에 적합한 진단 도구를 제시합니다. 실험 결과, CD는 편향된 MCMC에서 하이퍼파라미터 선택 시 기존 진단 방법보다 뛰어난 성능을 보였으며, 극단적 사건 행동을 구별하는 데 효과적입니다. CD는 기존의 Stein 기반 진단보다 계산 효율성이 높아 MCMC 실무자들에게 실질적인 가치를 제공합니다.

## 🎯 주요 포인트

- 1. 현대 베이지안 머신러닝의 기초가 되는 확장 가능한 MCMC 알고리즘은 계산 속도를 위해 비대칭성을 희생하며, 이는 전통적인 샘플 품질 측정이 실패하는 진단 격차를 초래합니다.
- 2. Copula Discrepancy (CD)는 샘플의 종속 구조의 충실도를 독립적으로 측정할 수 있는 효율적인 진단 도구로, Sklar의 정리를 활용합니다.
- 3. CD는 편향된 MCMC에서 하이퍼파라미터 선택 시 전통적인 진단 방법보다 우수한 성능을 보이며, 기존 방법이 실패하는 최적 구성을 정확히 식별합니다.
- 4. CD의 강력한 MLE 기반 변형은 랭크 상관 기반 접근법으로는 감지할 수 없는 꼬리 종속성의 미묘한 불일치를 감지할 수 있습니다.
- 5. CD는 기존의 Stein 불일치보다 훨씬 낮은 계산 오버헤드를 가지며, MCMC 실무자에게 실질적인 가치를 제공하고 구조 인식 샘플 품질 평가의 이론적 기반을 제공합니다.


---

*Generated on 2025-09-24 15:34:52*