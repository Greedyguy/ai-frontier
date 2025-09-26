---
keywords:
  - Smart Home IoT Devices
  - Latent Dirichlet Allocation
  - Transformer
  - Smart Home Security QA System
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19485
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:36:46.808288",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Smart Home IoT Devices",
    "Latent Dirichlet Allocation",
    "Transformer",
    "Smart Home Security QA System"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Smart Home IoT Devices": 0.8,
    "Latent Dirichlet Allocation": 0.85,
    "Transformer": 0.78,
    "Smart Home Security QA System": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "smart home IoT devices",
        "canonical": "Smart Home IoT Devices",
        "aliases": [
          "smart home devices",
          "IoT devices in smart homes"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on security concerns and is specific to the domain of smart homes.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Latent Dirichlet Allocation",
        "canonical": "Latent Dirichlet Allocation",
        "aliases": [
          "LDA"
        ],
        "category": "specific_connectable",
        "rationale": "LDA is a well-known technique for topic modeling, relevant for extracting security concerns.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "smaller transformer models",
        "canonical": "Transformer",
        "aliases": [
          "small transformer models",
          "T5",
          "Flan-T5"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a core technology in NLP, and the paper discusses their application in a specific context.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "QA system tailored for smart home security",
        "canonical": "Smart Home Security QA System",
        "aliases": [
          "QA system for smart home security"
        ],
        "category": "unique_technical",
        "rationale": "This system is a novel application of NLP techniques specifically for smart home security, enhancing its relevance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "security concerns",
      "dataset",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "smart home IoT devices",
      "resolved_canonical": "Smart Home IoT Devices",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Latent Dirichlet Allocation",
      "resolved_canonical": "Latent Dirichlet Allocation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "smaller transformer models",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "QA system tailored for smart home security",
      "resolved_canonical": "Smart Home Security QA System",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Identifying and Addressing User-level Security Concerns in Smart Homes Using "Smaller" LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19485.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19485](https://arxiv.org/abs/2509.19485)

## 🔗 유사한 논문
- [[2025-09-22/When Secure Isn't_ Assessing the Security of Machine Learning Model Sharing_20250922|When Secure Isn't: Assessing the Security of Machine Learning Model Sharing]] (82.1% similar)
- [[2025-09-24/Think in Safety_ Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model_20250924|Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model]] (81.0% similar)
- [[2025-09-23/Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis_20250923|Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis]] (80.4% similar)
- [[2025-09-23/SecureFixAgent_ A Hybrid LLM Agent for Automated Python Static Vulnerability Repair_20250923|SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair]] (79.6% similar)
- [[2025-09-19/Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems_20250919|Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Latent Dirichlet Allocation|Latent Dirichlet Allocation]]
**⚡ Unique Technical**: [[keywords/Smart Home IoT Devices|Smart Home IoT Devices]], [[keywords/Smart Home Security QA System|Smart Home Security QA System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19485v1 Announce Type: cross 
Abstract: With the rapid growth of smart home IoT devices, users are increasingly exposed to various security risks, as evident from recent studies. While seeking answers to know more on those security concerns, users are mostly left with their own discretion while going through various sources, such as online blogs and technical manuals, which may render higher complexity to regular users trying to extract the necessary information. This requirement does not go along with the common mindsets of smart home users and hence threatens the security of smart homes furthermore. In this paper, we aim to identify and address the major user-level security concerns in smart homes. Specifically, we develop a novel dataset of Q&amp;A from public forums, capturing practical security challenges faced by smart home users. We extract major security concerns in smart homes from our dataset by leveraging the Latent Dirichlet Allocation (LDA). We fine-tune relatively "smaller" transformer models, such as T5 and Flan-T5, on this dataset to build a QA system tailored for smart home security. Unlike larger models like GPT and Gemini, which are powerful but often resource hungry and require data sharing, smaller models are more feasible for deployment in resource-constrained or privacy-sensitive environments like smart homes. The dataset is manually curated and supplemented with synthetic data to explore its potential impact on model performance. This approach significantly improves the system's ability to deliver accurate and relevant answers, helping users address common security concerns with smart home IoT devices. Our experiments on real-world user concerns show that our work improves the performance of the base models.

## 📝 요약

이 논문은 스마트 홈 IoT 기기의 보안 문제를 사용자 관점에서 해결하기 위해 새로운 접근 방식을 제안합니다. 주요 기여는 사용자들이 직면하는 보안 문제를 파악하기 위해 공개 포럼의 Q&A 데이터를 수집하고, 이를 통해 주요 보안 우려 사항을 Latent Dirichlet Allocation(LDA)을 활용해 추출하는 것입니다. 또한, T5와 Flan-T5와 같은 소형 트랜스포머 모델을 이 데이터셋에 맞춰 미세 조정하여 스마트 홈 보안에 특화된 QA 시스템을 구축했습니다. 이 시스템은 자원 제한적이거나 프라이버시가 중요한 환경에서도 효과적으로 작동할 수 있으며, 실제 사용자 문제에 대한 실험 결과, 기존 모델의 성능을 개선하는 데 성공했습니다.

## 🎯 주요 포인트

- 1. 스마트 홈 IoT 기기의 보안 문제에 대한 사용자 수준의 주요 우려 사항을 식별하고 해결하는 것을 목표로 합니다.
- 2. 공개 포럼의 Q&A 데이터를 활용하여 스마트 홈 사용자들이 직면한 실질적인 보안 문제를 캡처한 새로운 데이터셋을 개발했습니다.
- 3. Latent Dirichlet Allocation (LDA)를 사용하여 스마트 홈의 주요 보안 문제를 추출했습니다.
- 4. T5 및 Flan-T5와 같은 상대적으로 작은 트랜스포머 모델을 데이터셋에 맞게 조정하여 스마트 홈 보안에 특화된 QA 시스템을 구축했습니다.
- 5. 실험 결과, 제안된 시스템이 스마트 홈 IoT 기기와 관련된 일반적인 보안 문제를 해결하는 데 있어 정확하고 관련성 높은 답변을 제공하는 능력을 크게 향상시켰습니다.


---

*Generated on 2025-09-25 15:36:46*