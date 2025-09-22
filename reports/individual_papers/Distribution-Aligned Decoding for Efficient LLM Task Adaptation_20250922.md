# Distribution-Aligned Decoding for Efficient LLM Task Adaptation

**Korean Title:** 분포 정렬 디코딩을 통한 효율적인 대형 언어 모델 과제 적응

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Kullback Leibler Divergence

## 🔗 유사한 논문
- [[2025-09-18/Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (84.0% similar)
- [[2025-09-22/On Optimal Steering to Achieve Exact Fairness_20250922|On Optimal Steering to Achieve Exact Fairness]] (83.5% similar)
- [[2025-09-18/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250918|Mind the Gap Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (83.2% similar)
- [[2025-09-19/Delta Knowledge Distillation for Large Language Models_20250919|Delta Knowledge Distillation for Large Language Models]] (83.1% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (82.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15888v1 Announce Type: cross 
Abstract: Adapting billion-parameter language models to a downstream task is still costly, even with parameter-efficient fine-tuning (PEFT). We re-cast task adaptation as output-distribution alignment: the objective is to steer the output distribution toward the task distribution directly during decoding rather than indirectly through weight updates. Building on this view, we introduce Steering Vector Decoding (SVD), a lightweight, PEFT-compatible, and theoretically grounded method. We start with a short warm-start fine-tune and extract a task-aware steering vector from the Kullback-Leibler (KL) divergence gradient between the output distribution of the warm-started and pre-trained models. This steering vector is then used to guide the decoding process to steer the model's output distribution towards the task distribution. We theoretically prove that SVD is first-order equivalent to the gradient step of full fine-tuning and derive a globally optimal solution for the strength of the steering vector. Across three tasks and nine benchmarks, SVD paired with four standard PEFT methods improves multiple-choice accuracy by up to 5 points and open-ended truthfulness by 2 points, with similar gains (1-2 points) on commonsense datasets without adding trainable parameters beyond the PEFT adapter. SVD thus offers a lightweight, theoretically grounded path to stronger task adaptation for large language models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15888v1 발표 유형: 교차  
초록: 수십억 개의 매개변수를 가진 언어 모델을 다운스트림 작업에 적응시키는 것은 여전히 비용이 많이 들며, 매개변수 효율적인 미세 조정(PEFT)을 사용하더라도 마찬가지입니다. 우리는 작업 적응을 출력 분포 정렬로 재구성합니다: 목표는 가중치 업데이트를 통해 간접적으로가 아니라 디코딩 중에 직접적으로 출력 분포를 작업 분포로 조정하는 것입니다. 이 관점을 바탕으로, 우리는 Steering Vector Decoding (SVD)라는 경량의, PEFT 호환 가능하며 이론적으로 근거 있는 방법을 소개합니다. 우리는 짧은 워밍업 미세 조정으로 시작하여 워밍업된 모델과 사전 훈련된 모델의 출력 분포 사이의 Kullback-Leibler (KL) 발산의 기울기에서 작업 인식 조정 벡터를 추출합니다. 그런 다음 이 조정 벡터를 사용하여 디코딩 과정을 안내하여 모델의 출력 분포를 작업 분포로 조정합니다. 우리는 SVD가 전체 미세 조정의 기울기 단계와 1차 동등함을 이론적으로 증명하고, 조정 벡터의 강도에 대한 전역 최적 솔루션을 도출합니다. 세 가지 작업과 아홉 가지 벤치마크에 걸쳐, SVD는 네 가지 표준 PEFT 방법과 결합하여 선택형 문제의 정확성을 최대 5점, 개방형 진실성을 2점까지 향상시키며, PEFT 어댑터 외에 학습 가능한 매개변수를 추가하지 않고도 상식 데이터셋에서 유사한 향상(1-2점)을 보입니다. 따라서 SVD는 대형 언어 모델의 더 강력한 작업 적응을 위한 경량의, 이론적으로 근거 있는 경로를 제공합니다.

## 📝 요약

이 논문은 대규모 언어 모델의 다운스트림 작업 적응을 위한 새로운 방법론인 Steering Vector Decoding (SVD)을 제안합니다. SVD는 출력 분포를 작업 분포에 직접 맞추는 방식으로, 파라미터 효율적 미세 조정(PEFT)과 호환됩니다. 초기 미세 조정 후 Kullback-Leibler 발산의 기울기를 이용해 작업 인식 조정 벡터를 추출하고, 이를 통해 모델의 출력 분포를 작업 분포로 유도합니다. 이 방법은 전체 미세 조정의 기울기 단계와 1차적으로 동등하며, 조정 벡터의 최적 강도를 이론적으로 도출합니다. 세 가지 작업과 아홉 개의 벤치마크에서 SVD는 PEFT 방법과 결합하여 선택형 정확도를 최대 5점, 개방형 진실성을 2점 향상시켰으며, 추가 학습 가능한 파라미터 없이 상식 데이터셋에서도 1-2점의 유사한 향상을 보였습니다. SVD는 대규모 언어 모델의 작업 적응을 강화하는 경량의 이론적 방법을 제공합니다.

## 🎯 주요 포인트

- 1. SVD(Steering Vector Decoding)는 대규모 언어 모델의 출력 분포를 직접 조정하여 다운스트림 작업에 적응시키는 경량화된 방법입니다.

- 2. SVD는 Kullback-Leibler(KL) 발산의 그래디언트를 활용하여 작업 인식 조정 벡터를 추출하고, 이를 통해 모델의 출력 분포를 작업 분포로 유도합니다.

- 3. SVD는 전체 미세 조정의 그래디언트 단계와 1차적으로 동등하며, 조정 벡터의 최적 강도를 이론적으로 도출합니다.

- 4. SVD는 세 가지 작업과 아홉 개의 벤치마크에서 다중 선택 정확도를 최대 5점, 개방형 진실성을 2점 향상시킵니다.

- 5. SVD는 추가 학습 가능한 매개변수를 도입하지 않고도 PEFT 어댑터와 함께 사용하여 상식 데이터셋에서 1-2점의 유사한 성능 향상을 제공합니다.

---

*Generated on 2025-09-22 14:15:24*