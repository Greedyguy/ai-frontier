# StreamBridge: Turning Your Offline Video Large Language Model into a Proactive Streaming Assistant

**Korean Title:** 스트림브리지: 오프라인 비디오 대형 언어 모델을 능동적인 스트리밍 보조 도구로 전환하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Memory Buffer, Proactive Response Mechanisms

## 🔗 유사한 논문
- [[2025-09-22/Efficient Real-time Refinement of Language Model Text Generation_20250922|Efficient Real-time Refinement of Language Model Text Generation]] (83.2% similar)
- [[2025-09-22/Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges_20250922|Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges]] (81.8% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.4% similar)
- [[2025-09-19/Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (80.4% similar)
- [[2025-09-22/Think, Verbalize, then Speak_ Bridging Complex Thoughts and Comprehensible Speech_20250922|Think, Verbalize, then Speak Bridging Complex Thoughts and Comprehensible Speech]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.05467v2 Announce Type: replace-cross 
Abstract: We present StreamBridge, a simple yet effective framework that seamlessly transforms offline Video-LLMs into streaming-capable models. It addresses two fundamental challenges in adapting existing models into online scenarios: (1) limited capability for multi-turn real-time understanding, and (2) lack of proactive response mechanisms. Specifically, StreamBridge incorporates (1) a memory buffer combined with a round-decayed compression strategy, supporting long-context multi-turn interactions, and (2) a decoupled, lightweight activation model that can be effortlessly integrated into existing Video-LLMs, enabling continuous proactive responses. To further support StreamBridge, we construct Stream-IT, a large-scale dataset tailored for streaming video understanding, featuring interleaved video-text sequences and diverse instruction formats. Extensive experiments show that StreamBridge significantly improves the streaming understanding capabilities of offline Video-LLMs across various tasks, outperforming even proprietary models such as GPT-4o and Gemini 1.5 Pro. Simultaneously, it achieves competitive or superior performance on standard video understanding benchmarks.

## 🔍 Abstract (한글 번역)

arXiv:2505.05467v2 발표 유형: 교차 대체  
초록: 우리는 StreamBridge라는 간단하지만 효과적인 프레임워크를 제시하여 오프라인 비디오-LLM을 스트리밍 가능한 모델로 원활하게 변환합니다. 이는 기존 모델을 온라인 시나리오에 적응시키는 데 있어 두 가지 근본적인 문제를 해결합니다: (1) 다중 턴 실시간 이해 능력의 제한, (2) 능동적인 응답 메커니즘의 부족. 구체적으로, StreamBridge는 (1) 메모리 버퍼와 라운드-디케이 압축 전략을 결합하여 긴 맥락의 다중 턴 상호작용을 지원하고, (2) 기존 비디오-LLM에 쉽게 통합할 수 있는 분리된 경량의 활성화 모델을 포함하여 지속적인 능동적 응답을 가능하게 합니다. StreamBridge를 더욱 지원하기 위해, 우리는 스트리밍 비디오 이해를 위한 대규모 데이터셋인 Stream-IT를 구축하였으며, 이는 비디오-텍스트 시퀀스와 다양한 지시 형식을 포함합니다. 광범위한 실험을 통해 StreamBridge가 다양한 작업에서 오프라인 비디오-LLM의 스트리밍 이해 능력을 크게 향상시키며, GPT-4o 및 Gemini 1.5 Pro와 같은 독점 모델을 능가함을 보여줍니다. 동시에 표준 비디오 이해 벤치마크에서도 경쟁력 있는 또는 우수한 성능을 달성합니다.

## 📝 요약

StreamBridge는 오프라인 비디오-LLM을 스트리밍 가능한 모델로 전환하는 간단하면서도 효과적인 프레임워크입니다. 이 연구는 (1) 실시간 다중 턴 이해 능력의 제한과 (2) 능동적 응답 메커니즘의 부족이라는 두 가지 주요 문제를 해결합니다. StreamBridge는 메모리 버퍼와 라운드-디케이 압축 전략을 사용하여 긴 문맥의 다중 턴 상호작용을 지원하고, 가벼운 활성화 모델을 통합하여 지속적인 능동적 응답을 가능하게 합니다. 또한, 스트리밍 비디오 이해를 위한 대규모 데이터셋인 Stream-IT를 구축하여 다양한 비디오-텍스트 시퀀스와 지시 형식을 제공합니다. 실험 결과, StreamBridge는 기존 모델보다 뛰어난 스트리밍 이해 능력을 보여주며, 표준 비디오 이해 벤치마크에서도 경쟁력 있는 성능을 발휘합니다.

## 🎯 주요 포인트

- 1. StreamBridge는 오프라인 Video-LLMs를 스트리밍 가능한 모델로 변환하는 간단하면서도 효과적인 프레임워크입니다.

- 2. StreamBridge는 다중 턴 실시간 이해 능력의 제한과 능동적 응답 메커니즘의 부족이라는 두 가지 주요 문제를 해결합니다.

- 3. 메모리 버퍼와 라운드-디케이 압축 전략을 통해 장기 문맥 다중 턴 상호작용을 지원합니다.

- 4. StreamBridge는 기존 Video-LLMs에 쉽게 통합될 수 있는 경량의 활성화 모델을 포함하여 지속적인 능동적 응답을 가능하게 합니다.

- 5. StreamBridge는 다양한 작업에서 오프라인 Video-LLMs의 스트리밍 이해 능력을 크게 향상시키며, GPT-4o 및 Gemini 1.5 Pro와 같은 독점 모델을 능가합니다.

---

*Generated on 2025-09-22 14:47:13*