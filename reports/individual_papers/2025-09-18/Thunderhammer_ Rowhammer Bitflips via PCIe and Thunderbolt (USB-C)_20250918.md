---
keywords:
  - Thunderhammer
  - Rowhammer
  - Thunderbolt
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.11440
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:04:37.826392",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Thunderhammer",
    "Rowhammer",
    "Thunderbolt"
  ],
  "rejected_keywords": [
    "PCIe"
  ],
  "similarity_scores": {
    "Thunderhammer": 0.85,
    "Rowhammer": 0.8,
    "Thunderbolt": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Thunderhammer: Rowhammer Bitflips via PCIe and Thunderbolt (USB-C)

**Korean Title:** 썬더해머: PCIe 및 썬더볼트 (USB-C)를 통한 로해머 비트 플립

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Thunderbolt|Thunderbolt]]
**⚡ Unique Technical**: [[keywords/Thunderhammer|Thunderhammer]], [[keywords/Rowhammer|Rowhammer]]

## 🔗 유사한 논문
- [[Protocol-Aware_Firmware_Rehosting_for_Effective_Fuzzing_of_Embedded_Network_Stacks_20250918|Protocol-Aware Firmware Rehosting for Effective Fuzzing of Embedded Network Stacks]] (73.4% similar)
- [[TFLAGTowards_Practical_APT_Detection_via_Deviation-Aware_Learning_on_Temporal_Provenance_Graph_20250918|TFLAG:Towards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph]] (72.4% similar)
- [[Multi-Threaded_Software_Model_Checking_via_Parallel_Trace_Abstraction_Refinement_20250918|Multi-Threaded Software Model Checking via Parallel Trace Abstraction Refinement]] (72.4% similar)
- [[Catalpa_GC_for_a_Low-Variance_Software_Stack_20250918|Catalpa: GC for a Low-Variance Software Stack]] (72.3% similar)
- [[GPU_Programming_for_AI_Workflow_Development_on_AWS_SageMaker_An_Instructional_Approach_20250918|GPU Programming for AI Workflow Development on AWS SageMaker: An Instructional Approach]] (72.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11440v2 Announce Type: replace 
Abstract: In recent years, Rowhammer has attracted significant attention from academia and industry alike. This technique, first published in 2014, flips bits in memory by repeatedly accessing neighbouring memory locations. Since its discovery, researchers have developed a substantial body of work exploiting Rowhammer and proposing countermeasures. These works demonstrate that Rowhammer can be mounted not only through native code, but also via remote code execution, such as JavaScript in browsers, and over networks.
  In this work, we uncover a previously unexplored Rowhammer vector. We present Thunderhammer, an attack that induces DRAM bitflips from malicious peripherals connected via PCIe or Thunderbolt (which tunnels PCIe). On modern DDR4 systems, we observe that triggering bitflips through PCIe requests requires precisely timed access patterns tailored to the target system. We design a custom device to reverse engineer critical architectural parameters that shape PCIe request scheduling, and to execute effective hammering access patterns. Leveraging this knowledge, we successfully demonstrate Rowhammer-induced bitflips in DDR4 memory modules via both PCIe slot connections and Thunderbolt ports tunnelling PCIe.

## 🔍 Abstract (한글 번역)

최근 몇 년간 Rowhammer 기술은 학계와 산업 모두의 주목을 받고 있습니다. 이 기술은 2014년 처음 발표되었으며, 인접한 메모리 위치를 반복적으로 액세스하여 메모리 내의 비트를 뒤집는 방법입니다. 이후 이 기술을 발견한 연구자들은 Rowhammer를 활용하고 대응책을 제안하는 방대한 연구를 수행해왔습니다. 이러한 연구들은 Rowhammer가 네이티브 코드뿐만 아니라 브라우저의 JavaScript와 네트워크를 통한 원격 코드 실행을 통해 공격될 수 있다는 것을 보여줍니다.

본 연구에서는 이전에 탐구되지 않았던 Rowhammer 벡터를 발견했습니다. 우리는 PCIe 또는 PCIe를 터널링하는 Thunderbolt를 통해 연결된 악의적인 주변 장치로부터 DRAM 비트 플립을 유발하는 공격인 Thunderhammer를 제시합니다. 현대의 DDR4 시스템에서는 PCIe 요청을 통해 비트 플립을 유발하기 위해서는 대상 시스템에 맞게 정확한 타이밍의 액세스 패턴이 필요합니다. 우리는 PCIe 요청 스케줄링을 결정하는 중요한 구조적 매개변수를 역공학하고 효과적인 해머링 액세스 패턴을 실행하기 위한 사용자 정의 장치를 설계했습니다. 이 지식을 활용하여 우리는 PCIe 슬롯 연결 및 PCIe를 터널링하는 Thunderbolt 포트를 통해 DDR4 메모리 모듈에서 Rowhammer에 의한 비트 플립을 성공적으로 시연했습니다.

## 📝 요약

이 연구는 최근 몇 년간 학계와 산업 모두에서 상당한 관심을 끌고 있는 Rowhammer 기술에 대해 다룬다. 이 기술은 2014년 처음 발표되었으며 인접한 메모리 위치를 반복적으로 액세스함으로써 메모리 내의 비트를 뒤집는다. 본 연구에서는 PCIe 또는 Thunderbolt를 통해 연결된 악의적인 주변기기로부터 DRAM 비트플립을 유도하는 Thunderhammer 공격을 제시한다. DDR4 시스템에서 PCIe 요청을 통해 비트플립을 유발하기 위해서는 대상 시스템에 맞춘 정확한 타이밍 액세스 패턴이 필요하다. 이를 위해 PCIe 요청 스케줄링을 형성하는 핵심 아키텍처 매개변수를 역공학하고 효과적인 해머링 액세스 패턴을 실행하기 위한 사용자 지정 장치를 설계한다. 이를 통해 PCIe 슬롯 연결 및 Thunderbolt 포트를 통한 DDR4 메모리 모듈에서 Rowhammer에 의한 비트플립을 성공적으로 시연한다.

## 🎯 주요 포인트

- 1. 최근 몇 년간 Rowhammer 기술이 학계와 산업에서 상당한 관심을 끌었다.

- 2. Thunderhammer를 통해 PCIe 또는 Thunderbolt를 통해 연결된 악의적인 주변 장치로부터 DRAM 비트 플립을 유도하는 공격을 제시한다.

- 3. DDR4 시스템에서 PCIe 요청을 통해 비트 플립을 유발하기 위해서는 대상 시스템에 맞게 조절된 정확한 타이밍 액세스 패턴이 필요하다.

---

*Generated on 2025-09-18 17:11:50*