
# Delta Knowledge Distillation for Large Language Models

**Korean Title:** 대형 언어 모델을 위한 델타 지식 증류

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Distributional Shift Preservation

## 🔗 유사한 논문
- [[KBM Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (83.2% similar)
- [[From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (83.0% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (79.4% similar)
- [[DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (78.9% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14526v1 Announce Type: cross 
Abstract: Knowledge distillation (KD) is a widely adopted approach for compressing large neural networks by transferring knowledge from a large teacher model to a smaller student model. In the context of large language models, token level KD, typically minimizing the KL divergence between student output distribution and teacher output distribution, has shown strong empirical performance. However, prior work assumes student output distribution and teacher output distribution share the same optimal representation space, a premise that may not hold in many cases. To solve this problem, we propose Delta Knowledge Distillation (Delta-KD), a novel extension of token level KD that encourages the student to approximate an optimal representation space by explicitly preserving the distributional shift Delta introduced during the teacher's supervised finetuning (SFT). Empirical results on ROUGE metrics demonstrate that Delta KD substantially improves student performance while preserving more of the teacher's knowledge.

## 🔍 Abstract (한글 번역)

arXiv:2509.14526v1 발표 유형: 교차  
초록: 지식 증류(Knowledge Distillation, KD)는 큰 신경망을 압축하기 위해 대형 교사 모델의 지식을 작은 학생 모델로 전이하는 널리 채택된 방법입니다. 대형 언어 모델의 맥락에서, 일반적으로 학생 출력 분포와 교사 출력 분포 간의 KL 발산을 최소화하는 토큰 수준의 KD는 강력한 경험적 성능을 보여주었습니다. 그러나 이전 연구에서는 학생 출력 분포와 교사 출력 분포가 동일한 최적의 표현 공간을 공유한다고 가정했는데, 이는 많은 경우에 성립하지 않을 수 있는 전제입니다. 이 문제를 해결하기 위해, 우리는 Delta Knowledge Distillation (Delta-KD)를 제안합니다. 이는 토큰 수준 KD의 새로운 확장으로, 학생이 교사의 감독된 미세 조정(SFT) 동안 도입된 분포적 변화 Delta를 명시적으로 보존함으로써 최적의 표현 공간을 근사하도록 장려합니다. ROUGE 지표에 대한 경험적 결과는 Delta KD가 학생의 성능을 상당히 향상시키면서 교사의 지식을 더 많이 보존함을 보여줍니다.

## 📝 요약

이 논문은 대형 언어 모델의 지식 증류(KD) 과정에서 발생하는 문제를 해결하기 위해 Delta Knowledge Distillation (Delta-KD)라는 새로운 방법론을 제안합니다. 기존의 토큰 수준 KD는 학생 모델과 교사 모델의 출력 분포가 동일한 최적의 표현 공간을 공유한다고 가정하지만, 이는 항상 성립하지 않습니다. Delta-KD는 교사의 지도 학습 과정에서 발생하는 분포 변화(Delta)를 명시적으로 보존하여 학생 모델이 최적의 표현 공간을 더 잘 근사하도록 유도합니다. 실험 결과, ROUGE 지표에서 Delta-KD가 학생 모델의 성능을 크게 향상시키면서 교사의 지식을 더 잘 보존함을 보여줍니다.

## 🎯 주요 포인트

- 1. 지식 증류(KD)는 큰 신경망을 압축하기 위해 대규모 교사 모델의 지식을 작은 학생 모델로 전이하는 방법이다.

- 2. 대규모 언어 모델에서 토큰 레벨 KD는 학생과 교사 출력 분포 간의 KL 발산을 최소화하여 강력한 성능을 보였다.

- 3. 기존 연구는 학생과 교사의 출력 분포가 동일한 최적의 표현 공간을 공유한다고 가정하지만, 이는 항상 성립하지 않는다.

- 4. Delta Knowledge Distillation(Delta-KD)은 교사의 감독된 미세 조정(SFT) 동안 도입된 분포 변화(Delta)를 명시적으로 보존하여 학생이 최적의 표현 공간을 근사하도록 유도하는 새로운 방법이다.

- 5. ROUGE 지표에 대한 실험 결과, Delta-KD는 학생의 성능을 크게 향상시키면서 교사의 지식을 더 많이 보존한다.

---

*Generated on 2025-09-19 14:56:43*