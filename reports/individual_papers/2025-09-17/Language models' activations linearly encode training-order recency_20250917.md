# Language models' activations linearly encode training-order recency

**Korean Title:** 언어 모델의 활성화는 훈련 순서의 최신성을 선형적으로 인코딩합니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Dmitrii Krasheninnikov|Dmitrii Krasheninnikov]] [[authors/Richard E. Turner|Richard E. Turner]] [[authors/David Krueger|David Krueger]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Temporal Encoding in Language Models

## 🔗 유사한 논문
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.4% similar)
- [[Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (80.9% similar)
- [[Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (80.6% similar)
- [[Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (80.3% similar)
- [[Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (80.2% similar)

## 📋 저자 정보

**Authors:** Dmitrii Krasheninnikov, Richard E. Turner, David Krueger

## 📄 Abstract (원문)

We show that language models' activations linearly encode when information
was learned during training. Our setup involves creating a model with a known
training order by sequentially fine-tuning Llama-3.2-1B on six disjoint but
otherwise similar datasets about named entities. We find that the average
activations of test samples for the six training datasets encode the training
order: when projected into a 2D subspace, these centroids are arranged exactly
in the order of training and lie on a straight line. Further, we show that
linear probes can accurately (~90%) distinguish "early" vs. "late" entities,
generalizing to entities unseen during the probes' own training. The model can
also be fine-tuned to explicitly report an unseen entity's training stage (~80%
accuracy). Interestingly, this temporal signal does not seem attributable to
simple differences in activation magnitudes, losses, or model confidence. Our
paper demonstrates that models are capable of differentiating information by
its acquisition time, and carries significant implications for how they might
manage conflicting data and respond to knowledge modifications.

## 🔍 Abstract (한글 번역)

언어 모델의 활성화가 학습 중 정보가 학습된 시점을 선형적으로 인코딩한다는 것을 보여줍니다. 우리의 설정은 Llama-3.2-1B를 여섯 개의 분리된, 그러나 유사한 명명된 엔티티에 관한 데이터셋에 순차적으로 파인튜닝하여 알려진 학습 순서를 가진 모델을 만드는 것을 포함합니다. 우리는 여섯 개의 학습 데이터셋에 대한 테스트 샘플의 평균 활성화가 학습 순서를 인코딩한다는 것을 발견했습니다. 2D 부분 공간으로 투영될 때, 이러한 중심점들은 정확히 학습 순서대로 배열되며 직선 위에 놓입니다. 더 나아가, 선형 프로브가 "초기"와 "후기" 엔티티를 약 90%의 정확도로 구별할 수 있으며, 프로브 자체의 학습 중 보지 못한 엔티티에도 일반화할 수 있음을 보여줍니다. 모델은 또한 보지 못한 엔티티의 학습 단계를 명시적으로 보고하도록 약 80%의 정확도로 파인튜닝될 수 있습니다. 흥미롭게도, 이러한 시간적 신호는 활성화 크기, 손실 또는 모델의 신뢰도와 같은 단순한 차이로 설명되지 않는 것으로 보입니다. 우리의 논문은 모델이 정보의 획득 시점에 따라 정보를 구별할 수 있음을 보여주며, 이는 모델이 상충되는 데이터를 관리하고 지식 수정에 대응하는 방식에 중대한 함의를 가집니다.

## 📝 요약

이 연구는 언어 모델의 활성화가 학습 중 정보가 습득된 시점을 선형적으로 인코딩할 수 있음을 보여줍니다. Llama-3.2-1B 모델을 여섯 개의 분리된 데이터셋으로 순차적으로 미세 조정하여 학습 순서를 설정했습니다. 실험 결과, 테스트 샘플의 평균 활성화가 학습 순서를 인코딩하며, 2D 공간에 투영했을 때 이 중심점들이 학습 순서대로 직선상에 배열됨을 발견했습니다. 또한, 선형 프로브를 통해 '초기'와 '후기' 엔티티를 약 90%의 정확도로 구별할 수 있으며, 이는 프로브 학습 시 보지 못한 엔티티에도 일반화됩니다. 모델은 보지 못한 엔티티의 학습 단계도 약 80%의 정확도로 보고할 수 있습니다. 이러한 시간 신호는 단순한 활성화 크기, 손실, 모델의 신뢰도 차이에 기인하지 않으며, 모델이 정보 습득 시점을 구별할 수 있음을 시사합니다. 이는 모델이 상충되는 데이터를 관리하고 지식 수정에 대응하는 방식에 중요한 함의를 가집니다.

## 🎯 주요 포인트

- 1. 언어 모델의 활성화는 정보가 학습된 시점을 선형적으로 인코딩할 수 있다.

- 2. Llama-3.2-1B 모델을 순차적으로 미세 조정하여 훈련 순서를 알 수 있는 설정을 만들었다.

- 3. 테스트 샘플의 평균 활성화가 훈련 순서를 인코딩하며, 이는 2D 서브스페이스에 투영될 때 훈련 순서대로 정렬된다.

- 4. 선형 프로브는 "초기"와 "후기" 엔티티를 약 90%의 정확도로 구분할 수 있다.

- 5. 모델은 보지 못한 엔티티의 훈련 단계를 약 80%의 정확도로 보고하도록 미세 조정될 수 있다.

---

*Generated on 2025-09-20 07:42:07*