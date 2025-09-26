---
keywords:
  - Large Language Models
  - Differential Privacy
  - Synthetic Data Generation
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:08:25.039524",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Differential Privacy",
    "Synthetic Data Generation"
  ],
  "rejected_keywords": [
    "Membership Inference Attack"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Differential Privacy": 0.78,
    "Synthetic Data Generation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# SynBench: A Benchmark for Differentially Private Text Generation

**Korean Title:** SynBench: 차등적으로 비공개 텍스트 생성을 위한 벤치마크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Differential Privacy|Differential Privacy]]
**⚡ Unique Technical**: [[keywords/Synthetic Data Generation|Synthetic Data Generation]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Practitioners' Perspectives on a Differential Privacy Deployment Registry_20250918|Practitioners' Perspectives on a Differential Privacy Deployment Registry]] (82.4% similar)
- [[MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (80.0% similar)
- [[Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (79.8% similar)
- [[The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (79.4% similar)
- [[SNaRe_ Domain-aware Data Generation for Low-Resource Event Detection_20250919|SNaRe Domain-aware Data Generation for Low-Resource Event Detection]] (79.0% similar)

## 📋 저자 정보

**Authors:** Yidan Sun, Viktor Schlegel, Srinivasan Nandakumar, Iqra Zahid, Yuping Wu, Yulong Wu, Hao Li, Jie Zhang, Warren Del-Pinto, Goran Nenadic, Siew Kei Lam, Anil Anthony Bharath

## 📄 Abstract (원문)

Data-driven decision support in high-stakes domains like healthcare and
finance faces significant barriers to data sharing due to regulatory,
institutional, and privacy concerns. While recent generative AI models, such as
large language models, have shown impressive performance in open-domain tasks,
their adoption in sensitive environments remains limited by unpredictable
behaviors and insufficient privacy-preserving datasets for benchmarking.
Existing anonymization methods are often inadequate, especially for
unstructured text, as redaction and masking can still allow re-identification.
Differential Privacy (DP) offers a principled alternative, enabling the
generation of synthetic data with formal privacy assurances. In this work, we
address these challenges through three key contributions. First, we introduce a
comprehensive evaluation framework with standardized utility and fidelity
metrics, encompassing nine curated datasets that capture domain-specific
complexities such as technical jargon, long-context dependencies, and
specialized document structures. Second, we conduct a large-scale empirical
study benchmarking state-of-the-art DP text generation methods and LLMs of
varying sizes and different fine-tuning strategies, revealing that high-quality
domain-specific synthetic data generation under DP constraints remains an
unsolved challenge, with performance degrading as domain complexity increases.
Third, we develop a membership inference attack (MIA) methodology tailored for
synthetic text, providing first empirical evidence that the use of public
datasets - potentially present in pre-training corpora - can invalidate claimed
privacy guarantees. Our findings underscore the urgent need for rigorous
privacy auditing and highlight persistent gaps between open-domain and
specialist evaluations, informing responsible deployment of generative AI in
privacy-sensitive, high-stakes settings.

## 🔍 Abstract (한글 번역)

고위험 분야인 의료 및 금융에서 데이터 기반 의사결정 지원은 규제, 기관, 개인정보 보호 문제로 인해 데이터 공유에 상당한 장벽에 직면하고 있습니다. 최근의 생성 AI 모델, 예를 들어 대규모 언어 모델은 개방형 도메인 작업에서 인상적인 성능을 보여주었지만, 민감한 환경에서의 채택은 예측 불가능한 행동과 벤치마킹을 위한 불충분한 개인정보 보호 데이터셋으로 인해 제한적입니다. 기존의 익명화 방법은 특히 비정형 텍스트의 경우 불충분한 경우가 많으며, 편집 및 마스킹이 재식별을 여전히 허용할 수 있습니다. 차등 개인정보 보호(Differential Privacy, DP)는 공식적인 개인정보 보호 보장을 통해 합성 데이터를 생성할 수 있는 원칙적인 대안을 제공합니다. 본 연구에서는 세 가지 주요 기여를 통해 이러한 문제를 해결합니다. 첫째, 기술적 전문 용어, 긴 문맥 의존성, 전문화된 문서 구조와 같은 도메인 특유의 복잡성을 포착하는 아홉 개의 큐레이션된 데이터셋을 포함하여 표준화된 유용성 및 충실도 메트릭을 갖춘 포괄적인 평가 프레임워크를 소개합니다. 둘째, 최첨단 DP 텍스트 생성 방법과 다양한 크기의 LLM 및 다양한 미세 조정 전략을 벤치마킹하는 대규모 실증 연구를 수행하여, 도메인 복잡성이 증가함에 따라 성능이 저하되는 DP 제약 하에서 고품질 도메인 특화 합성 데이터 생성이 여전히 해결되지 않은 과제임을 밝혀냅니다. 셋째, 합성 텍스트에 맞춤화된 멤버십 추론 공격(MIA) 방법론을 개발하여, 사전 학습 코퍼스에 존재할 가능성이 있는 공공 데이터셋의 사용이 주장된 개인정보 보호 보장을 무효화할 수 있다는 첫 실증적 증거를 제공합니다. 우리의 연구 결과는 엄격한 개인정보 보호 감사의 긴급한 필요성을 강조하며, 개방형 도메인과 전문 평가 간의 지속적인 격차를 부각시켜, 개인정보 보호가 중요한 고위험 환경에서 생성 AI의 책임 있는 배포를 위한 정보를 제공합니다.

## 📝 요약

이 논문은 의료 및 금융과 같은 고위험 분야에서 데이터 공유의 어려움을 해결하기 위해 차별적 프라이버시(DP)를 활용한 데이터 생성 방법을 제안합니다. 주요 기여는 다음과 같습니다. 첫째, 기술 용어와 긴 문맥 의존성을 포함한 9개의 데이터셋을 사용하여 평가 프레임워크를 구축했습니다. 둘째, 최신 DP 텍스트 생성 방법과 다양한 크기의 대형 언어 모델(LLM)을 비교한 결과, DP 제약하에서 고품질의 도메인 특화 데이터 생성이 여전히 어려운 과제임을 발견했습니다. 셋째, 합성 텍스트에 대한 멤버십 추론 공격 방법론을 개발하여, 공개 데이터셋 사용이 프라이버시 보장을 무효화할 수 있음을 입증했습니다. 이러한 결과는 프라이버시 감사를 강화하고, 민감한 환경에서 생성 AI의 책임 있는 배포를 위한 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 데이터 공유의 어려움으로 인해 의료 및 금융과 같은 고위험 분야에서 데이터 기반 의사결정 지원이 제한되고 있습니다.

- 2. 기존 익명화 방법은 비정형 텍스트에서 재식별 위험이 있어 충분하지 않으며, 차등 개인정보 보호(DP)는 형식적인 개인정보 보호를 보장하는 합성 데이터 생성을 가능하게 합니다.

- 3. 본 연구는 기술적 용어, 긴 문맥 의존성, 전문 문서 구조 등 도메인 특성을 반영한 9개의 데이터셋을 포함하는 평가 프레임워크를 소개합니다.

- 4. 차등 개인정보 보호 제약 하에서의 고품질 도메인 특화 합성 데이터 생성은 여전히 해결되지 않은 과제로 남아 있으며, 도메인 복잡성이 증가할수록 성능이 저하됩니다.

- 5. 합성 텍스트에 대한 멤버십 추론 공격(MIA) 방법론을 개발하여, 공개 데이터셋의 사용이 개인정보 보호 보장을 무효화할 수 있음을 처음으로 실증적으로 입증하였습니다.

---

*Generated on 2025-09-20 05:50:45*