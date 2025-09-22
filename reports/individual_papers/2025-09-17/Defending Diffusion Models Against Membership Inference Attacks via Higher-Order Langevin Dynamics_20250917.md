# Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics

**Korean Title:** 확산 모델을 고차 랑주뱅 동역학을 통해 멤버십 추론 공격으로부터 방어하기

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Benjamin Sterling|Benjamin Sterling]] [[authors/Yousef El-Laham|Yousef El-Laham]] [[authors/Mónica F. Bugallo|Mónica F. Bugallo]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Critically-Damped Langevin Dynamics

## 🔗 유사한 논문
- [[Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (81.5% similar)
- [[SynBench_ A Benchmark for Differentially Private Text Generation_20250918|SynBench A Benchmark for Differentially Private Text Generation]] (81.1% similar)
- [[Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (81.1% similar)
- [[The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (80.8% similar)
- [[Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (80.8% similar)

## 📋 저자 정보

**Authors:** Benjamin Sterling, Yousef El-Laham, Mónica F. Bugallo

## 📄 Abstract (원문)

Recent advances in generative artificial intelligence applications have
raised new data security concerns. This paper focuses on defending diffusion
models against membership inference attacks. This type of attack occurs when
the attacker can determine if a certain data point was used to train the model.
Although diffusion models are intrinsically more resistant to membership
inference attacks than other generative models, they are still susceptible. The
defense proposed here utilizes critically-damped higher-order Langevin
dynamics, which introduces several auxiliary variables and a joint diffusion
process along these variables. The idea is that the presence of auxiliary
variables mixes external randomness that helps to corrupt sensitive input data
earlier on in the diffusion process. This concept is theoretically investigated
and validated on a toy dataset and a speech dataset using the Area Under the
Receiver Operating Characteristic (AUROC) curves and the FID metric.

## 🔍 Abstract (한글 번역)

최근 생성적 인공지능 응용 프로그램의 발전은 새로운 데이터 보안 문제를 제기했습니다. 이 논문은 확산 모델을 회원 추론 공격으로부터 방어하는 데 중점을 두고 있습니다. 회원 추론 공격은 공격자가 특정 데이터 포인트가 모델 훈련에 사용되었는지를 판단할 수 있는 경우 발생합니다. 확산 모델은 본질적으로 다른 생성 모델보다 회원 추론 공격에 더 저항력이 있지만, 여전히 취약할 수 있습니다. 여기서 제안된 방어 방법은 비평형 고차 랑주뱅 역학을 활용하여 여러 보조 변수를 도입하고 이 변수들에 대한 공동 확산 과정을 포함합니다. 보조 변수의 존재는 외부 무작위성을 혼합하여 확산 과정 초기에 민감한 입력 데이터를 손상시키는 데 도움을 줍니다. 이 개념은 이론적으로 조사되었으며, 수신자 조작 특성 (ROC) 곡선 아래 면적 (AUROC)과 FID 지표를 사용하여 장난감 데이터셋과 음성 데이터셋에서 검증되었습니다.

## 📝 요약

이 논문은 생성 인공지능 모델의 데이터 보안 문제를 다루며, 특히 확산 모델을 대상으로 한 멤버십 추론 공격 방어에 중점을 둡니다. 확산 모델은 본래 다른 생성 모델보다 멤버십 추론 공격에 강하지만 여전히 취약성이 존재합니다. 이를 방어하기 위해, 논문은 비평형 고차 랑주뱅 동역학을 활용하여 여러 보조 변수를 도입하고 이들 변수와의 공동 확산 과정을 제안합니다. 이러한 보조 변수는 외부 무작위성을 혼합하여 민감한 입력 데이터를 초기 단계에서 손상시키는 역할을 합니다. 이 방법은 이론적으로 분석되었으며, 장난감 데이터셋과 음성 데이터셋을 통해 AUROC 곡선과 FID 지표를 사용하여 검증되었습니다.

## 🎯 주요 포인트

- 1. 생성적 인공지능의 발전은 새로운 데이터 보안 문제를 야기하고 있다.

- 2. 본 논문은 멤버십 추론 공격에 대한 확산 모델의 방어에 초점을 맞추고 있다.

- 3. 제안된 방어 기법은 비평형 고차 랑주뱅 동역학을 활용하여 민감한 입력 데이터를 초기 확산 과정에서 혼합 및 손상시킨다.

- 4. 이 방어 기법은 이론적으로 연구되었으며, 장난감 데이터셋과 음성 데이터셋에서 AUROC 곡선과 FID 지표를 사용하여 검증되었다.

---

*Generated on 2025-09-20 07:41:43*