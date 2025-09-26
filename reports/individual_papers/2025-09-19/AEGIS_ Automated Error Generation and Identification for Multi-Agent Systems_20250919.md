---
keywords:
  - Multi-Agent Systems
  - Automated Error Generation and Identification
  - Large Language Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14295
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:58:56.445621",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Agent Systems",
    "Automated Error Generation and Identification",
    "Large Language Models"
  ],
  "rejected_keywords": [
    "Reinforcement Learning"
  ],
  "similarity_scores": {
    "Multi-Agent Systems": 0.85,
    "Automated Error Generation and Identification": 0.8,
    "Large Language Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# AEGIS: Automated Error Generation and Identification for Multi-Agent Systems

**Korean Title:** AEGIS: 다중 에이전트 시스템을 위한 자동 오류 생성 및 식별

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Multi-Agent Systems|Multi-Agent Systems]], [[keywords/Automated Error Generation and Identification|Automated Error Generation and Identification]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Who is Introducing the Failure_ Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis_20250918|Who is Introducing the Failure Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis]] (83.9% similar)
- [[Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems_20250919|Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems]] (82.6% similar)
- [[AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (82.5% similar)
- [[Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents_20250919|Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents]] (82.1% similar)
- [[An Empirical Study on Failures in Automated Issue Solving]] (81.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14295v1 Announce Type: new 
Abstract: As Multi-Agent Systems (MAS) become increasingly autonomous and complex, understanding their error modes is critical for ensuring their reliability and safety. However, research in this area has been severely hampered by the lack of large-scale, diverse datasets with precise, ground-truth error labels. To address this bottleneck, we introduce \textbf{AEGIS}, a novel framework for \textbf{A}utomated \textbf{E}rror \textbf{G}eneration and \textbf{I}dentification for Multi-Agent \textbf{S}ystems. By systematically injecting controllable and traceable errors into initially successful trajectories, we create a rich dataset of realistic failures. This is achieved using a context-aware, LLM-based adaptive manipulator that performs sophisticated attacks like prompt injection and response corruption to induce specific, predefined error modes. We demonstrate the value of our dataset by exploring three distinct learning paradigms for the error identification task: Supervised Fine-Tuning, Reinforcement Learning, and Contrastive Learning. Our comprehensive experiments show that models trained on AEGIS data achieve substantial improvements across all three learning paradigms. Notably, several of our fine-tuned models demonstrate performance competitive with or superior to proprietary systems an order of magnitude larger, validating our automated data generation framework as a crucial resource for developing more robust and interpretable multi-agent systems. Our project website is available at https://kfq20.github.io/AEGIS-Website.

## 🔍 Abstract (한글 번역)

arXiv:2509.14295v1 발표 유형: 신규  
초록: 다중 에이전트 시스템(Multi-Agent Systems, MAS)이 점점 더 자율적이고 복잡해짐에 따라, 이들의 오류 모드를 이해하는 것은 신뢰성과 안전성을 보장하기 위해 매우 중요합니다. 그러나 이 분야의 연구는 정확한 실제 오류 레이블을 갖춘 대규모의 다양한 데이터셋이 부족하여 심각한 제약을 받고 있습니다. 이러한 병목 현상을 해결하기 위해, 우리는 다중 에이전트 시스템을 위한 \textbf{자동화된 오류 생성 및 식별}(Automated Error Generation and Identification for Multi-Agent Systems, \textbf{AEGIS})이라는 새로운 프레임워크를 소개합니다. 초기 성공 경로에 제어 가능하고 추적 가능한 오류를 체계적으로 주입함으로써, 현실적인 실패의 풍부한 데이터셋을 생성합니다. 이는 특정한 사전 정의된 오류 모드를 유도하기 위해 프롬프트 주입 및 응답 손상과 같은 정교한 공격을 수행하는 문맥 인식 LLM 기반의 적응형 조작기를 사용하여 달성됩니다. 우리는 오류 식별 작업을 위한 세 가지 학습 패러다임인 지도 학습 세부 조정(Supervised Fine-Tuning), 강화 학습(Reinforcement Learning), 대조 학습(Contrastive Learning)을 탐구함으로써 데이터셋의 가치를 입증합니다. 우리의 포괄적인 실험은 AEGIS 데이터로 훈련된 모델이 세 가지 학습 패러다임 모두에서 상당한 개선을 이룬다는 것을 보여줍니다. 특히, 우리의 세부 조정된 여러 모델은 규모가 훨씬 큰 독점 시스템과 경쟁하거나 이를 능가하는 성능을 보여주며, 우리의 자동화된 데이터 생성 프레임워크가 보다 견고하고 해석 가능한 다중 에이전트 시스템 개발을 위한 중요한 자원임을 입증합니다. 우리의 프로젝트 웹사이트는 https://kfq20.github.io/AEGIS-Website에서 확인할 수 있습니다.

## 📝 요약

이 논문은 다중 에이전트 시스템(MAS)의 신뢰성과 안전성을 보장하기 위해 오류 모드를 이해하는 것이 중요하다고 강조합니다. 이를 위해 \textbf{AEGIS}라는 새로운 프레임워크를 소개하며, 이는 자동화된 오류 생성 및 식별을 통해 대규모의 다양한 오류 데이터를 생성합니다. 이 프레임워크는 LLM 기반의 적응형 조작기를 사용하여 특정 오류 모드를 유도하는 정교한 공격을 수행합니다. 연구는 이 데이터셋을 활용하여 지도 학습, 강화 학습, 대조 학습의 세 가지 학습 패러다임에서 오류 식별 성능을 향상시켰음을 보여줍니다. 특히, AEGIS 데이터로 학습된 모델들이 훨씬 큰 규모의 독점 시스템과 비교해 경쟁력 있는 성능을 보였으며, 이는 자동화된 데이터 생성 프레임워크의 중요성을 입증합니다.

## 🎯 주요 포인트

- 1. 다중 에이전트 시스템의 신뢰성과 안전성을 보장하기 위해 오류 모드를 이해하는 것이 중요합니다.

- 2. AEGIS는 다중 에이전트 시스템을 위한 자동 오류 생성 및 식별을 위한 새로운 프레임워크입니다.

- 3. AEGIS는 성공적인 경로에 오류를 주입하여 현실적인 실패 데이터를 생성합니다.

- 4. AEGIS 데이터로 학습한 모델은 세 가지 학습 패러다임에서 성능이 크게 개선되었습니다.

- 5. AEGIS는 더 견고하고 해석 가능한 다중 에이전트 시스템 개발에 중요한 자원으로 입증되었습니다.

---

*Generated on 2025-09-19 16:28:27*