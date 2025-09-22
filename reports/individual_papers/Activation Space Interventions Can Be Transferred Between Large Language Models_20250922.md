# Activation Space Interventions Can Be Transferred Between Large Language Models

**Korean Title:** 활성화 공간 개입은 대형 언어 모델 간에 전이될 수 있다.

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Lightweight Safety Switches

## 🔗 유사한 논문
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (83.4% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (83.0% similar)
- [[2025-09-18/MUSE_ MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models_20250918|MUSE MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models]] (82.4% similar)
- [[2025-09-18/Is GPT-4o mini Blinded by its Own Safety Filters Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection_20250918|Is GPT-4o mini Blinded by its Own Safety Filters Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection]] (82.3% similar)
- [[2025-09-19/Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (82.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.04429v4 Announce Type: replace 
Abstract: The study of representation universality in AI models reveals growing convergence across domains, modalities, and architectures. However, the practical applications of representation universality remain largely unexplored. We bridge this gap by demonstrating that safety interventions can be transferred between models through learned mappings of their shared activation spaces. We demonstrate this approach on two well-established AI safety tasks: backdoor removal and refusal of harmful prompts, showing successful transfer of steering vectors that alter the models' outputs in a predictable way. Additionally, we propose a new task, \textit{corrupted capabilities}, where models are fine-tuned to embed knowledge tied to a backdoor. This tests their ability to separate useful skills from backdoors, reflecting real-world challenges. Extensive experiments across Llama, Qwen and Gemma model families show that our method enables using smaller models to efficiently align larger ones. Furthermore, we demonstrate that autoencoder mappings between base and fine-tuned models can serve as reliable ``lightweight safety switches", allowing dynamic toggling between model behaviors.

## 🔍 Abstract (한글 번역)

arXiv:2503.04429v4 발표 유형: 교체  
초록: AI 모델에서의 표현 보편성 연구는 도메인, 모달리티, 아키텍처 전반에 걸쳐 점점 더 많은 수렴을 보여줍니다. 그러나 표현 보편성의 실제 응용은 아직 대부분 탐구되지 않았습니다. 우리는 모델의 공유 활성화 공간에 대한 학습된 매핑을 통해 안전 개입이 모델 간에 전이될 수 있음을 증명함으로써 이 격차를 해소합니다. 우리는 두 가지 잘 확립된 AI 안전 작업, 즉 백도어 제거와 유해한 프롬프트 거부에서 이 접근 방식을 시연하며, 모델의 출력을 예측 가능한 방식으로 변경하는 조정 벡터의 성공적인 전이를 보여줍니다. 또한, 우리는 백도어와 연결된 지식을 내재화하도록 모델을 미세 조정하는 새로운 작업인 \textit{손상된 기능}을 제안합니다. 이는 유용한 기술을 백도어로부터 분리하는 모델의 능력을 테스트하며, 이는 실제 세계의 도전 과제를 반영합니다. Llama, Qwen, Gemma 모델 계열 전반에 걸친 광범위한 실험은 우리의 방법이 더 작은 모델을 사용하여 더 큰 모델을 효율적으로 정렬할 수 있게 함을 보여줍니다. 더욱이, 기본 모델과 미세 조정된 모델 간의 오토인코더 매핑이 신뢰할 수 있는 "경량 안전 스위치"로 작용할 수 있음을 보여주며, 모델 행동 간의 동적 전환을 허용합니다.

## 📝 요약

이 논문은 AI 모델의 표현 보편성을 활용하여 안전 개입을 모델 간에 전이할 수 있는 방법을 제시합니다. 연구는 백도어 제거와 유해한 프롬프트 거부라는 두 가지 AI 안전 과제에서 모델의 출력 변화를 예측 가능한 방식으로 유도하는 벡터 전이의 성공을 보여줍니다. 또한, 새로운 과제인 '손상된 능력'을 제안하여 백도어와 연결된 지식을 임베딩하는 모델의 능력을 테스트합니다. 실험 결과, Llama, Qwen, Gemma 모델군에서 작은 모델을 사용해 큰 모델을 효율적으로 조정할 수 있음을 확인했습니다. 더불어, 기본 모델과 미세 조정된 모델 간의 오토인코더 매핑이 신뢰할 수 있는 경량 안전 스위치로 작용할 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. AI 모델의 표현 보편성 연구는 도메인, 모달리티, 아키텍처 간의 수렴을 보여주지만, 실제 응용은 아직 탐구되지 않았다.

- 2. 본 연구는 모델 간의 공유 활성화 공간을 통한 학습 매핑을 통해 안전 개입을 전이할 수 있음을 입증한다.

- 3. 백도어 제거 및 유해한 프롬프트 거부와 같은 AI 안전 작업에서 모델 출력의 예측 가능한 변화를 유도하는 조정 벡터의 성공적인 전이를 보여준다.

- 4. 새로운 과제인 '손상된 역량'을 제안하여 모델이 백도어와 관련된 지식을 내재화하도록 미세 조정하고, 유용한 기술과 백도어를 분리하는 능력을 테스트한다.

- 5. Llama, Qwen, Gemma 모델 계열의 광범위한 실험을 통해 작은 모델을 사용하여 더 큰 모델을 효율적으로 정렬할 수 있음을 보여준다.

---

*Generated on 2025-09-22 14:30:41*