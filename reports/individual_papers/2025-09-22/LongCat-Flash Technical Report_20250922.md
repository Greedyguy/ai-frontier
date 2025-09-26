---
keywords:
  - Mixture-of-Experts
  - Zero-computation Experts
  - Shortcut-connected Mixture-of-Experts
  - Scalable Efficiency
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.01322
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:10:31.422239",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture-of-Experts",
    "Zero-computation Experts",
    "Shortcut-connected Mixture-of-Experts",
    "Scalable Efficiency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixture-of-Experts": 0.82,
    "Zero-computation Experts": 0.78,
    "Shortcut-connected Mixture-of-Experts": 0.77,
    "Scalable Efficiency": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mixture-of-Experts",
        "canonical": "Mixture-of-Experts",
        "aliases": [
          "MoE"
        ],
        "category": "specific_connectable",
        "rationale": "Mixture-of-Experts models are a significant architectural choice in machine learning, facilitating connections with other models using similar architectures.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Zero-computation Experts",
        "canonical": "Zero-computation Experts",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This novel design within the LongCat-Flash model is unique and could be pivotal for understanding its efficiency innovations.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "Shortcut-connected MoE",
        "canonical": "Shortcut-connected Mixture-of-Experts",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This specific architectural enhancement is critical for the model's efficiency and provides a unique linking opportunity.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "scalable efficiency",
        "canonical": "Scalable Efficiency",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Scalable efficiency is a broad technical concept that underpins many advancements in large-scale models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "computational efficiency",
      "advanced agentic capabilities"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Mixture-of-Experts",
      "resolved_canonical": "Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Zero-computation Experts",
      "resolved_canonical": "Zero-computation Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Shortcut-connected MoE",
      "resolved_canonical": "Shortcut-connected Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "scalable efficiency",
      "resolved_canonical": "Scalable Efficiency",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# LongCat-Flash Technical Report

**Korean Title:** 롱캣-플래시 기술 보고서

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.01322.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.01322](https://arxiv.org/abs/2509.01322)

## 🔗 유사한 논문
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment]] (80.8% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (80.8% similar)
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (80.1% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (79.8% similar)
- [[2025-09-18/CSMoE_ An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts_20250918|CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Scalable Efficiency|Scalable Efficiency]]
**🔗 Specific Connectable**: [[keywords/Mixture-of-Experts|Mixture-of-Experts]]
**⚡ Unique Technical**: [[keywords/Zero-computation Experts|Zero-computation Experts]], [[keywords/Shortcut-connected Mixture-of-Experts|Shortcut-connected Mixture-of-Experts]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.01322v2 Announce Type: replace-cross 
Abstract: We introduce LongCat-Flash, a 560-billion-parameter Mixture-of-Experts (MoE) language model designed for both computational efficiency and advanced agentic capabilities. Stemming from the need for scalable efficiency, LongCat-Flash adopts two novel designs: (a) Zero-computation Experts, which enables dynamic computational budget allocation and activates 18.6B-31.3B (27B on average) per token depending on contextual demands, optimizing resource usage. (b) Shortcut-connected MoE, which enlarges the computation-communication overlap window, demonstrating notable gains in inference efficiency and throughput compared to models of a comparable scale. We develop a comprehensive scaling framework for large models that combines hyperparameter transfer, model-growth initialization, a multi-pronged stability suite, and deterministic computation to achieve stable and reproducible training. Notably, leveraging the synergy among scalable architectural design and infrastructure efforts, we complete model training on more than 20 trillion tokens within 30 days, while achieving over 100 tokens per second (TPS) for inference at a cost of \$0.70 per million output tokens. To cultivate LongCat-Flash towards agentic intelligence, we conduct a large-scale pre-training on optimized mixtures, followed by targeted mid- and post-training on reasoning, code, and instructions, with further augmentation from synthetic data and tool use tasks. Comprehensive evaluations demonstrate that, as a non-thinking foundation model, LongCat-Flash delivers highly competitive performance among other leading models, with exceptional strengths in agentic tasks. The model checkpoint of LongCat-Flash is open-sourced to foster community research.
  LongCat Chat: https://longcat.ai
  Hugging Face: https://huggingface.co/meituan-longcat
  GitHub: https://github.com/meituan-longcat

## 🔍 Abstract (한글 번역)

arXiv:2509.01322v2 발표 유형: 교차 대체

초록: 우리는 계산 효율성과 고급 에이전트 기능을 모두 갖춘 5600억 매개변수의 전문가 혼합(MoE) 언어 모델인 LongCat-Flash를 소개합니다. 확장 가능한 효율성의 필요성에서 출발하여, LongCat-Flash는 두 가지 새로운 설계를 채택합니다: (a) 제로 계산 전문가, 이는 동적 계산 예산 할당을 가능하게 하며, 문맥적 요구에 따라 토큰당 18.6B-31.3B(평균 27B)를 활성화하여 자원 사용을 최적화합니다. (b) 숏컷 연결 MoE, 이는 계산-통신 중첩 창을 확장하여, 유사한 규모의 모델에 비해 추론 효율성과 처리량에서 주목할 만한 향상을 보여줍니다. 우리는 대형 모델을 위한 포괄적인 확장 프레임워크를 개발하여, 하이퍼파라미터 전이, 모델 성장 초기화, 다각적 안정성 스위트, 결정론적 계산을 결합하여 안정적이고 재현 가능한 훈련을 달성합니다. 특히, 확장 가능한 아키텍처 설계와 인프라 노력 간의 시너지를 활용하여, 30일 이내에 20조 이상의 토큰에 대한 모델 훈련을 완료하고, 초당 100개 이상의 토큰(TPS)을 초당 0.70달러의 비용으로 추론하여 출력 토큰 백만 개당 비용을 달성합니다. LongCat-Flash를 에이전트 지능으로 발전시키기 위해, 최적화된 혼합물에 대한 대규모 사전 훈련을 수행하고, 추론, 코드 및 지침에 대한 목표 중간 및 후속 훈련을 수행하며, 합성 데이터 및 도구 사용 작업으로 추가 강화합니다. 포괄적인 평가 결과, LongCat-Flash는 비사고 기반 모델로서 다른 선도적인 모델들 사이에서 매우 경쟁력 있는 성능을 제공하며, 에이전트 작업에서 뛰어난 강점을 보입니다. LongCat-Flash의 모델 체크포인트는 커뮤니티 연구를 촉진하기 위해 오픈 소스로 제공됩니다.

LongCat Chat: https://longcat.ai  
Hugging Face: https://huggingface.co/meituan-longcat  
GitHub: https://github.com/meituan-longcat

## 📝 요약

LongCat-Flash는 5600억 개의 파라미터를 가진 Mixture-of-Experts(MoE) 언어 모델로, 계산 효율성과 고급 에이전트 기능을 목표로 설계되었습니다. 주요 기여로는 (a) Zero-computation Experts를 통해 문맥에 따라 동적으로 계산 자원을 할당하여 평균 27억 개의 파라미터를 활성화하고, (b) Shortcut-connected MoE를 통해 계산과 통신의 중첩을 확대하여 추론 효율성을 향상시킨 점이 있습니다. 모델은 30일 내에 20조 개 이상의 토큰으로 훈련되었으며, 1초당 100개 이상의 토큰을 생성할 수 있습니다. LongCat-Flash는 대규모 사전 훈련과 추가적인 코드 및 명령어 학습을 통해 에이전트 지능을 강화하였으며, 평가 결과 다른 선도 모델들과 비교해 뛰어난 성능을 보였습니다. 모델 체크포인트는 오픈 소스로 제공되어 연구 커뮤니티의 발전을 지원합니다.

## 🎯 주요 포인트

- 1. LongCat-Flash는 5600억 매개변수를 가진 Mixture-of-Experts(MoE) 언어 모델로, 계산 효율성과 고급 에이전트 기능을 목표로 설계되었습니다.
- 2. Zero-computation Experts 설계를 통해 문맥에 따라 동적으로 계산 자원을 할당하여 평균 270억 매개변수를 활성화하고 자원 사용을 최적화합니다.
- 3. Shortcut-connected MoE 설계는 계산-통신 중첩 창을 확장하여 유사 규모 모델 대비 추론 효율성과 처리량에서 유의미한 향상을 보여줍니다.
- 4. 30일 내에 20조 개 이상의 토큰을 학습하고, 초당 100개 이상의 토큰을 추론하며, 백만 개 출력 토큰당 \$0.70의 비용으로 효율적인 추론을 달성했습니다.
- 5. LongCat-Flash는 에이전트 지능을 목표로 대규모 사전 학습과 중간 및 후속 학습을 통해 경쟁력 있는 성능을 발휘하며, 특히 에이전트 작업에서 뛰어난 강점을 보입니다.


---

*Generated on 2025-09-23 10:10:31*