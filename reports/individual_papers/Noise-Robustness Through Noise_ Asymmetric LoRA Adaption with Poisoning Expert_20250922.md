# Noise-Robustness Through Noise: Asymmetric LoRA Adaption with Poisoning Expert

**Korean Title:** 소음에 의한 소음 견고성: 중독 전문가를 통한 비대칭 LoRA 적응

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Noise Robust Adaptation

## 🔗 유사한 논문
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (82.7% similar)
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (80.2% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (80.0% similar)
- [[2025-09-18/Not All Degradations Are Equal_ A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution_20250918|Not All Degradations Are Equal A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution]] (79.7% similar)
- [[2025-09-18/LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (79.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23868v4 Announce Type: replace-cross 
Abstract: Current parameter-efficient fine-tuning methods for adapting pre-trained language models to downstream tasks are susceptible to interference from noisy data. Conventional noise-handling approaches either rely on laborious data pre-processing or employ model architecture modifications prone to error accumulation. In contrast to existing noise-process paradigms, we propose a noise-robust adaptation method via asymmetric LoRA poisoning experts (LoPE), a novel framework that enhances model robustness to noise only with generated noisy data. Drawing inspiration from the mixture-of-experts architecture, LoPE strategically integrates a dedicated poisoning expert in an asymmetric LoRA configuration. Through a two-stage paradigm, LoPE performs noise injection on the poisoning expert during fine-tuning to enhance its noise discrimination and processing ability. During inference, we selectively mask the dedicated poisoning expert to leverage purified knowledge acquired by normal experts for noise-robust output. Extensive experiments demonstrate that LoPE achieves strong performance and robustness purely through the low-cost noise injection, which completely eliminates the requirement of data cleaning.

## 🔍 Abstract (한글 번역)

arXiv:2505.23868v4 발표 유형: 교차 교체  
초록: 사전 학습된 언어 모델을 다운스트림 작업에 적응시키기 위한 현재의 매개변수 효율적 미세 조정 방법은 잡음이 많은 데이터로부터의 간섭에 취약합니다. 기존의 잡음 처리 접근법은 번거로운 데이터 전처리에 의존하거나 오류 누적에 취약한 모델 아키텍처 수정을 사용합니다. 기존의 잡음 처리 패러다임과 달리, 우리는 생성된 잡음 데이터만으로 모델의 잡음에 대한 강건성을 향상시키는 비대칭 LoRA 중독 전문가(LoPE)를 통한 잡음 강건 적응 방법을 제안합니다. 전문가 혼합 아키텍처에서 영감을 받아, LoPE는 비대칭 LoRA 구성에서 전용 중독 전문가를 전략적으로 통합합니다. 두 단계 패러다임을 통해, LoPE는 미세 조정 중 중독 전문가에 대한 잡음 주입을 수행하여 잡음 판별 및 처리 능력을 향상시킵니다. 추론 시, 우리는 전용 중독 전문가를 선택적으로 마스킹하여 정상 전문가가 획득한 정제된 지식을 활용하여 잡음 강건 출력을 생성합니다. 광범위한 실험을 통해 LoPE는 데이터 정리의 필요성을 완전히 제거하는 저비용 잡음 주입만으로 강력한 성능과 강건성을 달성함을 입증합니다.

## 📝 요약

이 논문은 사전 학습된 언어 모델을 다운스트림 작업에 적응시키는 과정에서 발생하는 노이즈 문제를 해결하기 위한 새로운 방법론을 제안합니다. 기존의 노이즈 처리 방법은 데이터 전처리나 모델 구조 변경에 의존하여 오류가 발생할 가능성이 높습니다. 이에 반해, 저자들은 비대칭 LoRA 포이즈닝 전문가(LoPE)를 활용한 노이즈에 강한 적응 방법을 제시합니다. LoPE는 전문가 혼합 구조에서 영감을 받아, 비대칭 LoRA 구성에서 포이즈닝 전문가를 통합합니다. 이 방법은 두 단계로 이루어지며, 미세 조정 과정에서 포이즈닝 전문가에 노이즈를 주입하여 노이즈 식별 및 처리 능력을 향상시킵니다. 추론 시에는 포이즈닝 전문가를 선택적으로 마스킹하여 정제된 지식을 활용합니다. 실험 결과, LoPE는 데이터 정제 없이도 강력한 성능과 노이즈에 대한 견고함을 저비용으로 달성함을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존의 파라미터 효율적 미세 조정 방법은 노이즈 데이터에 취약하며, 일반적인 노이즈 처리 방법은 데이터 전처리나 모델 구조 수정에 의존합니다.

- 2. 제안된 LoPE(비대칭 LoRA 중독 전문가)는 생성된 노이즈 데이터만으로 모델의 노이즈에 대한 강건성을 향상시키는 새로운 프레임워크입니다.

- 3. LoPE는 전문가 혼합 아키텍처에서 영감을 받아, 비대칭 LoRA 구성에서 전용 중독 전문가를 통합하여 노이즈 주입을 통해 노이즈 구별 및 처리 능력을 강화합니다.

- 4. 추론 시, 전용 중독 전문가를 선택적으로 마스킹하여 정규 전문가가 습득한 정제된 지식을 활용하여 노이즈에 강건한 출력을 생성합니다.

- 5. 광범위한 실험 결과, LoPE는 저비용의 노이즈 주입만으로도 강력한 성능과 강건성을 달성하며, 데이터 정제의 필요성을 완전히 제거합니다.

---

*Generated on 2025-09-22 14:52:02*