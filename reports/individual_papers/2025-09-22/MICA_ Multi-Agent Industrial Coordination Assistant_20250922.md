---
keywords:
  - Multi-Agent Coordination
  - Adaptive Step Fusion
  - Multi-Agent Coordination Benchmark
  - Natural Language Processing
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15237
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:42:48.051111",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Agent Coordination",
    "Adaptive Step Fusion",
    "Multi-Agent Coordination Benchmark",
    "Natural Language Processing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Agent Coordination": 0.8,
    "Adaptive Step Fusion": 0.78,
    "Multi-Agent Coordination Benchmark": 0.75,
    "Natural Language Processing": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Agent Industrial Coordination Assistant",
        "canonical": "Multi-Agent Coordination",
        "aliases": [
          "MICA"
        ],
        "category": "unique_technical",
        "rationale": "This is a central concept of the paper, introducing a novel system for industrial environments.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adaptive Step Fusion",
        "canonical": "Adaptive Step Fusion",
        "aliases": [
          "ASF"
        ],
        "category": "unique_technical",
        "rationale": "Represents a new method for integrating expert reasoning with speech feedback, crucial for understanding the paper's contributions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "multi-agent coordination benchmark",
        "canonical": "Multi-Agent Coordination Benchmark",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a new benchmark for evaluating multi-agent systems, which is a significant contribution to the field.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "natural speech feedback",
        "canonical": "Natural Language Processing",
        "aliases": [
          "speech feedback"
        ],
        "category": "broad_technical",
        "rationale": "Links to the broader field of NLP, which is relevant for understanding the speech-interactive aspect of the system.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "task success",
      "real-time guidance",
      "offline hardware"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Agent Industrial Coordination Assistant",
      "resolved_canonical": "Multi-Agent Coordination",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adaptive Step Fusion",
      "resolved_canonical": "Adaptive Step Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multi-agent coordination benchmark",
      "resolved_canonical": "Multi-Agent Coordination Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "natural speech feedback",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# MICA: Multi-Agent Industrial Coordination Assistant

**Korean Title:** MICA: 다중 에이전트 산업 조정 보조 시스템

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15237.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15237](https://arxiv.org/abs/2509.15237)

## 🔗 유사한 논문
- [[2025-09-18/InfraMind_ A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management_20250918|InfraMind: A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management]] (83.6% similar)
- [[2025-09-19/Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems_20250919|Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems]] (82.4% similar)
- [[2025-09-18/MAFA_ A multi-agent framework for annotation_20250918|MAFA: A multi-agent framework for annotation]] (82.3% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (82.1% similar)
- [[2025-09-22/Explainable AI-Enhanced Supervisory Control for Robust Multi-Agent Robotic Systems_20250922|Explainable AI-Enhanced Supervisory Control for Robust Multi-Agent Robotic Systems]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**⚡ Unique Technical**: [[keywords/Multi-Agent Coordination|Multi-Agent Coordination]], [[keywords/Adaptive Step Fusion|Adaptive Step Fusion]], [[keywords/Multi-Agent Coordination Benchmark|Multi-Agent Coordination Benchmark]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15237v1 Announce Type: new 
Abstract: Industrial workflows demand adaptive and trustworthy assistance that can operate under limited computing, connectivity, and strict privacy constraints. In this work, we present MICA (Multi-Agent Industrial Coordination Assistant), a perception-grounded and speech-interactive system that delivers real-time guidance for assembly, troubleshooting, part queries, and maintenance. MICA coordinates five role-specialized language agents, audited by a safety checker, to ensure accurate and compliant support. To achieve robust step understanding, we introduce Adaptive Step Fusion (ASF), which dynamically blends expert reasoning with online adaptation from natural speech feedback. Furthermore, we establish a new multi-agent coordination benchmark across representative task categories and propose evaluation metrics tailored to industrial assistance, enabling systematic comparison of different coordination topologies. Our experiments demonstrate that MICA consistently improves task success, reliability, and responsiveness over baseline structures, while remaining deployable on practical offline hardware. Together, these contributions highlight MICA as a step toward deployable, privacy-preserving multi-agent assistants for dynamic factory environments. The source code will be made publicly available at https://github.com/Kratos-Wen/MICA.

## 🔍 Abstract (한글 번역)

arXiv:2509.15237v1 발표 유형: 신규  
초록: 산업 워크플로우는 제한된 컴퓨팅, 연결성, 엄격한 개인정보 보호 제약 조건 하에서 작동할 수 있는 적응적이고 신뢰할 수 있는 지원을 요구합니다. 본 연구에서는 조립, 문제 해결, 부품 문의 및 유지보수에 대한 실시간 지침을 제공하는 인식 기반 및 음성 상호작용 시스템인 MICA(Multi-Agent Industrial Coordination Assistant)를 소개합니다. MICA는 안전 검사자가 감사하는 다섯 개의 역할 전문화된 언어 에이전트를 조정하여 정확하고 준수하는 지원을 보장합니다. 견고한 단계 이해를 달성하기 위해, 우리는 전문가의 추론과 자연어 피드백으로부터의 온라인 적응을 동적으로 혼합하는 Adaptive Step Fusion(ASF)을 도입합니다. 또한, 대표적인 작업 범주에 걸친 새로운 다중 에이전트 조정 벤치마크를 설정하고, 산업 지원에 맞춘 평가 지표를 제안하여 다양한 조정 토폴로지를 체계적으로 비교할 수 있게 합니다. 우리의 실험은 MICA가 기본 구조에 비해 작업 성공률, 신뢰성 및 응답성을 지속적으로 향상시키면서도 실용적인 오프라인 하드웨어에서 배포 가능함을 보여줍니다. 이러한 기여는 MICA가 동적 공장 환경을 위한 배포 가능하고 개인정보를 보호하는 다중 에이전트 어시스턴트로 나아가는 한 걸음을 강조합니다. 소스 코드는 https://github.com/Kratos-Wen/MICA에서 공개될 예정입니다.

## 📝 요약

이 논문에서는 제한된 컴퓨팅 및 연결 환경과 엄격한 개인정보 보호 조건 하에서 작동할 수 있는 적응적이고 신뢰할 수 있는 산업용 지원 시스템 MICA를 소개합니다. MICA는 실시간 조립, 문제 해결, 부품 조회 및 유지보수 지원을 제공하는 인식 기반 음성 상호작용 시스템입니다. 다섯 개의 역할 특화 언어 에이전트를 조정하고 안전 검사자가 이를 검토하여 정확하고 규정 준수하는 지원을 보장합니다. 강력한 단계 이해를 위해 자연어 피드백을 통해 전문가의 추론과 온라인 적응을 동적으로 결합하는 Adaptive Step Fusion(ASF)을 도입했습니다. 또한, 대표적인 작업 범주에 걸친 새로운 다중 에이전트 조정 벤치마크를 설정하고 산업 지원에 맞춘 평가 지표를 제안하여 다양한 조정 구조를 체계적으로 비교할 수 있게 했습니다. 실험 결과, MICA는 기존 구조에 비해 작업 성공률, 신뢰성 및 응답성을 꾸준히 향상시키며 실제 오프라인 하드웨어에서 배포 가능합니다. 이러한 기여는 MICA가 동적 공장 환경을 위한 배포 가능하고 개인정보를 보호하는 다중 에이전트 지원 시스템으로 발전하는 데 기여함을 강조합니다. 소스 코드는 [GitHub 링크](https://github.com/Kratos-Wen/MICA)에서 공개될 예정입니다.

## 🎯 주요 포인트

- 1. MICA는 제한된 컴퓨팅, 연결성, 엄격한 개인정보 보호 조건 하에서 작동할 수 있는 적응적이고 신뢰할 수 있는 산업 워크플로우 지원 시스템입니다.
- 2. MICA는 조립, 문제 해결, 부품 조회 및 유지보수에 대한 실시간 지침을 제공하는 다중 에이전트 시스템으로, 안전 검사자가 검토하는 다섯 개의 역할 특화 언어 에이전트를 조정합니다.
- 3. 적응형 단계 융합(ASF)을 도입하여 전문가의 추론과 자연어 음성 피드백을 통한 온라인 적응을 동적으로 결합하여 강력한 단계 이해를 달성합니다.
- 4. 대표적인 작업 카테고리 전반에 걸쳐 새로운 다중 에이전트 조정 벤치마크를 설정하고, 산업 지원에 맞춘 평가 지표를 제안하여 다양한 조정 구조의 체계적인 비교를 가능하게 합니다.
- 5. 실험 결과, MICA는 기본 구조에 비해 작업 성공률, 신뢰성, 응답성을 지속적으로 개선하면서도 실용적인 오프라인 하드웨어에 배포할 수 있음을 보여줍니다.


---

*Generated on 2025-09-23 08:42:48*