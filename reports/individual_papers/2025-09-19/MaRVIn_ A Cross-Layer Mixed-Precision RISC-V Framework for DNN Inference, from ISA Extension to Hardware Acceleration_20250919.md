---
keywords:
  - RISC-V Architectures
  - Deep Learning
  - Mixed-Precision Techniques
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15187
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:35:42.608064",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "RISC-V Architectures",
    "Deep Learning",
    "Mixed-Precision Techniques"
  ],
  "rejected_keywords": [
    "Hardware-Software Co-Design",
    "Cycle-Accurate Emulation"
  ],
  "similarity_scores": {
    "RISC-V Architectures": 0.8,
    "Deep Learning": 0.85,
    "Mixed-Precision Techniques": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# MaRVIn: A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration

**Korean Title:** MaRVIn: ISA 확장부터 하드웨어 가속까지 DNN 추론을 위한 크로스 레이어 혼합 정밀도 RISC-V 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|deep learning inference]]
**🔗 Specific Connectable**: [[keywords/RISC-V Architectures|RISC-V architectures]]
**⚡ Unique Technical**: [[keywords/Mixed-Precision Techniques|mixed-precision techniques]]

## 🔗 유사한 논문
- [[Evolution of Kernels Automated RISC-V Kernel Optimization with Large Language Models]] (83.5% similar)
- [[eIQ Neutron Redefining Edge-AI Inference with Integrated NPU and Compiler Innovations]] (81.5% similar)
- [[Task-Aware_Image_Signal_Processor_for_Advanced_Visual_Perception_20250918|Task-Aware Image Signal Processor for Advanced Visual Perception]] (80.5% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (79.9% similar)
- [[NIRVANA Structured pruning reimagined for large language models compression]] (79.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15187v1 Announce Type: new 
Abstract: The evolution of quantization and mixed-precision techniques has unlocked new possibilities for enhancing the speed and energy efficiency of NNs. Several recent studies indicate that adapting precision levels across different parameters can maintain accuracy comparable to full-precision models while significantly reducing computational demands. However, existing embedded microprocessors lack sufficient architectural support for efficiently executing mixed-precision NNs, both in terms of ISA extensions and hardware design, resulting in inefficiencies such as excessive data packing/unpacking and underutilized arithmetic units. In this work, we propose novel ISA extensions and a micro-architecture implementation specifically designed to optimize mixed-precision execution, enabling energy-efficient deep learning inference on RISC-V architectures. We introduce MaRVIn, a cross-layer hardware-software co-design framework that enhances power efficiency and performance through a combination of hardware improvements, mixed-precision quantization, ISA-level optimizations, and cycle-accurate emulation. At the hardware level, we enhance the ALU with configurable mixed-precision arithmetic (2, 4, 8 bits) for weights/activations and employ multi-pumping to reduce execution latency while implementing soft SIMD for efficient 2-bit ops. At the software level, we integrate a pruning-aware fine-tuning method to optimize model compression and a greedy-based DSE approach to efficiently search for Pareto-optimal mixed-quantized models. Additionally, we incorporate voltage scaling to boost the power efficiency of our system. Our experimental evaluation over widely used DNNs and datasets, such as CIFAR10 and ImageNet, demonstrates that our framework can achieve, on average, 17.6x speedup for less than 1% accuracy loss and outperforms the ISA-agnostic state-of-the-art RISC-V cores, delivering up to 1.8 TOPs/W.

## 🔍 Abstract (한글 번역)

arXiv:2509.15187v1 발표 유형: 신규  
초록: 양자화 및 혼합 정밀도 기술의 발전은 신경망(NN)의 속도와 에너지 효율성을 향상시킬 수 있는 새로운 가능성을 열었습니다. 최근 여러 연구에 따르면, 다양한 매개변수에 걸쳐 정밀도 수준을 조정하면 전체 정밀도 모델과 유사한 정확도를 유지하면서도 계산 요구를 크게 줄일 수 있습니다. 그러나 기존의 임베디드 마이크로프로세서는 ISA 확장과 하드웨어 설계 측면에서 혼합 정밀도 NN을 효율적으로 실행하기 위한 충분한 아키텍처 지원이 부족하여 과도한 데이터 패킹/언패킹 및 산술 유닛의 활용 부족과 같은 비효율성을 초래합니다. 본 연구에서는 RISC-V 아키텍처에서 에너지 효율적인 심층 학습 추론을 가능하게 하는 혼합 정밀도 실행을 최적화하기 위해 특별히 설계된 새로운 ISA 확장 및 마이크로 아키텍처 구현을 제안합니다. 우리는 하드웨어 개선, 혼합 정밀도 양자화, ISA 수준 최적화 및 주기 정확한 에뮬레이션을 결합하여 전력 효율성과 성능을 향상시키는 크로스 레이어 하드웨어-소프트웨어 공동 설계 프레임워크인 MaRVIn을 소개합니다. 하드웨어 수준에서는 가중치/활성화에 대해 구성 가능한 혼합 정밀도 산술(2, 4, 8비트)을 갖춘 ALU를 개선하고, 실행 지연을 줄이기 위해 멀티 펌핑을 사용하며, 효율적인 2비트 연산을 위한 소프트 SIMD를 구현합니다. 소프트웨어 수준에서는 모델 압축을 최적화하기 위해 가지치기 인식 미세 조정 방법을 통합하고, 파레토 최적 혼합 양자화 모델을 효율적으로 탐색하기 위한 탐욕 기반 DSE 접근 방식을 통합합니다. 또한, 시스템의 전력 효율성을 높이기 위해 전압 스케일링을 도입합니다. CIFAR10 및 ImageNet과 같은 널리 사용되는 DNN 및 데이터셋에 대한 실험적 평가 결과, 우리의 프레임워크는 평균적으로 1% 미만의 정확도 손실로 17.6배의 속도 향상을 달성할 수 있으며, ISA에 구애받지 않는 최신 RISC-V 코어를 능가하여 최대 1.8 TOPs/W를 제공합니다.

## 📝 요약

이 논문은 혼합 정밀도 신경망(NN)의 효율적인 실행을 위한 새로운 ISA 확장과 마이크로아키텍처 구현을 제안합니다. 기존 임베디드 마이크로프로세서는 혼합 정밀도 NN 실행에 필요한 아키텍처 지원이 부족하여 비효율성이 발생합니다. 이를 해결하기 위해 MaRVIn이라는 하드웨어-소프트웨어 공동 설계 프레임워크를 도입하여 RISC-V 아키텍처에서 에너지 효율적인 딥러닝 추론을 가능하게 합니다. 하드웨어 측면에서는 가중치/활성화에 대해 2, 4, 8비트의 혼합 정밀도 연산을 지원하는 ALU를 개선하고, 소프트 SIMD를 활용하여 2비트 연산을 효율적으로 수행합니다. 소프트웨어 측면에서는 가지치기 인식 미세 조정 방법과 탐욕 기반 설계 공간 탐색(DSE)을 통해 모델 압축을 최적화합니다. 실험 결과, 제안된 프레임워크는 평균 17.6배의 속도 향상을 이루며, 1% 미만의 정확도 손실로 최신 RISC-V 코어를 능가하는 성능을 보입니다.

## 🎯 주요 포인트

- 1. 혼합 정밀도 기술을 활용하여 RISC-V 아키텍처에서 에너지 효율적인 딥러닝 추론을 가능하게 하는 새로운 ISA 확장과 마이크로 아키텍처 구현을 제안합니다.

- 2. MaRVIn은 하드웨어 개선, 혼합 정밀도 양자화, ISA 수준 최적화, 사이클 정확한 에뮬레이션을 통해 전력 효율성과 성능을 향상시키는 하드웨어-소프트웨어 공동 설계 프레임워크입니다.

- 3. 하드웨어 수준에서 가중치/활성화에 대해 2, 4, 8비트의 구성 가능한 혼합 정밀도 산술을 ALU에 추가하고, 다중 펌핑을 사용하여 실행 지연을 줄이며, 효율적인 2비트 연산을 위한 소프트 SIMD를 구현합니다.

- 4. 소프트웨어 수준에서 모델 압축을 최적화하기 위한 가지치기 인식 미세 조정 방법과 파레토 최적의 혼합 양자화 모델을 효율적으로 탐색하기 위한 탐욕 기반 DSE 접근 방식을 통합합니다.

- 5. 제안된 프레임워크는 CIFAR10 및 ImageNet과 같은 널리 사용되는 DNN 및 데이터셋에서 평균 17.6배의 속도 향상을 이루며, ISA 비의존적 최신 RISC-V 코어를 능가하여 최대 1.8 TOPs/W의 성능을 제공합니다.

---

*Generated on 2025-09-19 15:32:35*