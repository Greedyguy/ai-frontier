---
keywords:
  - Fuzz Testing
  - Firmware Rehosting
  - Embedded Network Stacks
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13740
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:14:40.863101",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fuzz Testing",
    "Firmware Rehosting",
    "Embedded Network Stacks"
  ],
  "rejected_keywords": [
    "Network Protocols"
  ],
  "similarity_scores": {
    "Fuzz Testing": 0.8,
    "Firmware Rehosting": 0.78,
    "Embedded Network Stacks": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Protocol-Aware Firmware Rehosting for Effective Fuzzing of Embedded Network Stacks

**Korean Title:** 효과적인 임베디드 네트워크 스택 퍼징을 위한 프로토콜 인식 펌웨어 재호스팅

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Fuzz Testing|fuzz testing]]
**⚡ Unique Technical**: [[keywords/Firmware Rehosting|firmware rehosting]], [[keywords/Embedded Network Stacks|embedded network stacks]]

## 🔗 유사한 논문
- [[BERTector_An_Intrusion_Detection_Framework_Constructed_via_Joint-dataset_Learning_Based_on_Language_Model_20250918|BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (75.3% similar)
- [[An Empirical Study on Failures in Automated Issue Solving]] (75.2% similar)
- [[The_Cybersecurity_of_a_Humanoid_Robot_20250918|The Cybersecurity of a Humanoid Robot]] (75.1% similar)
- [[CyberLLMInstruct: A Pseudo-malicious Dataset Revealing Safety-performance Trade-offs in Cyber Security LLM Fine-tuning]] (73.6% similar)
- [[Thunderhammer_Rowhammer_Bitflips_via_PCIe_and_Thunderbolt_(USB-C)_20250918|Thunderhammer: Rowhammer Bitflips via PCIe and Thunderbolt (USB-C)]] (73.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13740v1 Announce Type: new 
Abstract: One of the biggest attack surfaces of embedded systems is their network interfaces, which enable communication with other devices. Unlike their general-purpose counterparts, embedded systems are designed for specialized use cases, resulting in unique and diverse communication stacks. Unfortunately, current approaches for evaluating the security of these embedded network stacks require manual effort or access to hardware, and they generally focus only on small parts of the embedded system. A promising alternative is firmware rehosting, which enables fuzz testing of the entire firmware by generically emulating the physical hardware. However, existing rehosting methods often struggle to meaningfully explore network stacks due to their complex, multi-layered input formats. This limits their ability to uncover deeply nested software faults.
  To address this problem, we introduce a novel method to automatically detect and handle the use of network protocols in firmware called Pemu. By automatically deducing the available network protocols, Pemu can transparently generate valid network packets that encapsulate fuzzing data, allowing the fuzzing input to flow directly into deeper layers of the firmware logic. Our approach thus enables a deeper, more targeted, and layer-by-layer analysis of firmware components that were previously difficult or impossible to test. Our evaluation demonstrates that Pemu consistently improves the code coverage of three existing rehosting tools for embedded network stacks. Furthermore, our fuzzer rediscovered several known vulnerabilities and identified five previously unknown software faults, highlighting its effectiveness in uncovering deeply nested bugs in network-exposed code.

## 🔍 Abstract (한글 번역)

arXiv:2509.13740v1 발표 유형: 새로운
요약: 임베디드 시스템의 가장 큰 공격 표면 중 하나는 다른 장치와의 통신을 가능하게 하는 네트워크 인터페이스입니다. 일반 목적용 시스템과 달리 임베디드 시스템은 특수한 용도를 위해 설계되어 고유하고 다양한 통신 스택을 가지고 있습니다. 안타깝게도, 현재 임베디드 네트워크 스택의 보안을 평가하는 방법은 수동 노력이 필요하거나 하드웨어에 액세스해야 하며, 일반적으로 임베디드 시스템의 작은 부분에만 초점을 맞춥니다. 유망한 대안은 펌웨어 재호스팅으로, 물리적 하드웨어를 일반적으로 에뮬레이션하여 전체 펌웨어의 퍼징 테스트를 가능하게 합니다. 그러나 기존의 재호스팅 방법은 복잡하고 다층적인 입력 형식으로 인해 네트워크 스택을 의미 있는 방식으로 탐색하는 데 어려움을 겪습니다. 이는 깊게 중첩된 소프트웨어 결함을 발견하는 능력을 제한합니다.
이 문제를 해결하기 위해, 우리는 Pemu라는 펌웨어에서 네트워크 프로토콜 사용을 자동으로 감지하고 처리하는 새로운 방법을 소개합니다. Pemu는 사용 가능한 네트워크 프로토콜을 자동으로 추론하여 퍼징 데이터를 캡슐화하는 유효한 네트워크 패킷을 투명하게 생성할 수 있어, 퍼징 입력이 퍼웨어 로직의 더 깊은 레이어로 직접 흐를 수 있습니다. 우리의 접근법은 이전에 테스트하기 어렵거나 불가능했던 펌웨어 구성 요소의 더 깊고 명확하며 레이어별 분석을 가능하게 합니다. 우리의 평가는 Pemu가 임베디드 네트워크 스택을 위한 세 가지 기존 재호스팅 도구의 코드 커버리지를 일관되게 향상시킨다는 것을 보여줍니다. 더욱이, 우리의 퍼저는 몇 가지 알려진 취약점을 재발견하고 이전에 알려지지 않았던 다섯 가지 소프트웨어 결함을 식별하여, 네트워크 노출 코드의 깊게 중첩된 버그를 발견하는 데 효과적임을 강조합니다.

## 📝 요약

임베디드 시스템의 가장 큰 공격 표면 중 하나는 다른 장치와의 통신을 가능케 하는 네트워크 인터페이스이다. 현재 임베디드 네트워크 스택의 보안을 평가하는 방법은 수동 작업이 필요하거나 하드웨어에 접근해야 하는 등 제약이 많다. 본 연구에서는 Pemu라는 새로운 방법을 제안하여 firmware 내의 네트워크 프로토콜 사용을 자동으로 감지하고 처리함으로써 임베디드 네트워크 스택의 보안 측면을 개선하였다. Pemu는 유효한 네트워크 패킷을 생성하여 fuzzing 데이터를 캡슐화하고 firmware 로직의 깊은 레이어로 직접 흘려보내는 것을 가능케 한다. 이를 통해 기존 방법론보다 더 깊고 목표적인 firmware 구성 요소의 분석이 가능해졌으며, 이로써 네트워크 노출 코드의 깊게 중첩된 버그를 발견하는 효과적인 방법임을 입증하였다.

## 🎯 주요 포인트

- 임베디드 시스템의 네트워크 인터페이스는 공격 표면 중 하나로, 특수한 용도로 설계되어 고유하고 다양한 통신 스택을 가지고 있다.

- 기존 방법론은 수동 노력이 필요하거나 하드웨어 접근이 필요하며, 주로 임베디드 시스템의 작은 부분에만 초점을 맞춘다.

- Pemu는 네트워크 프로토콜 사용을 자동으로 감지하고 처리하는 혁신적인 방법론으로, 펌웨어 로직의 깊은 레이어로 직접 흐르는 퍼징 입력을 허용한다.

---

*Generated on 2025-09-18 17:09:06*