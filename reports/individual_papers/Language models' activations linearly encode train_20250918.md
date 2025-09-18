
# Language models' activations linearly encode training-order recency

**Korean Title:** 언어 모델의 활성화는 훈련 순서의 최신성을 선형적으로 부호화합니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Temporal signal|Temporal signal]] [[keywords/broad/Language models|Language models]] [[keywords/broad/Training-order recency|Training-order recency]] [[keywords/specific/Linear probes|Linear probes]] [[keywords/unique/Llama-3.2-1B|Llama-3.2-1B]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Sequential fine-tuning
**🔬 Broad Technical**: Language models, Training-order recency
**🔗 Specific Connectable**: Linear probes
**⭐ Unique Technical**: Llama-3.2-1B

**ArXiv ID**: [2509.14223](https://arxiv.org/abs/2509.14223)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.14223.pdf)


## 🏷️ 추출된 키워드



`Language models` • 

`Training-order recency` • 

`Linear probes` • 

`Llama-3.2-1B` • 

`Temporal signal`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14223v1 Announce Type: cross 
Abstract: We show that language models' activations linearly encode when information was learned during training. Our setup involves creating a model with a known training order by sequentially fine-tuning Llama-3.2-1B on six disjoint but otherwise similar datasets about named entities. We find that the average activations of test samples for the six training datasets encode the training order: when projected into a 2D subspace, these centroids are arranged exactly in the order of training and lie on a straight line. Further, we show that linear probes can accurately (~90%) distinguish "early" vs. "late" entities, generalizing to entities unseen during the probes' own training. The model can also be fine-tuned to explicitly report an unseen entity's training stage (~80% accuracy). Interestingly, this temporal signal does not seem attributable to simple differences in activation magnitudes, losses, or model confidence. Our paper demonstrates that models are capable of differentiating information by its acquisition time, and carries significant implications for how they might manage conflicting data and respond to knowledge modifications.

## 🔍 Abstract (한글 번역)

arXiv:2509.14223v1 발표 유형: 교차
요약: 우리는 언어 모델의 활성화가 훈련 중에 정보가 언제 배워졌는지를 선형적으로 인코딩한다는 것을 보여줍니다. 우리의 설정은 명명된 엔티티에 관한 여섯 가지 겹치지 않는 그러나 그 외 유사한 데이터셋에서 순차적으로 Llama-3.2-1B를 파인튜닝하여 알려진 훈련 순서를 가진 모델을 만드는 것을 포함합니다. 우리는 여섯 가지 훈련 데이터셋의 테스트 샘플들의 평균 활성화가 훈련 순서를 인코딩한다는 것을 발견했습니다: 2D 부분 공간으로 투영될 때, 이러한 중심점은 훈련 순서대로 정확히 배열되어 있고 직선상에 위치합니다. 더 나아가, 우리는 선형 프로브가 "이른" vs. "늦은" 엔티티를 정확하게(~90%) 구별할 수 있음을 보여주며, 프로브 자체의 훈련 중에 보지 못한 엔티티에 대해 일반화됩니다. 모델은 또한 보고되지 않은 엔티티의 훈련 단계를 명시적으로 보고할 수 있습니다(~80% 정확도). 흥미로운 점은, 이 시간 신호가 활성화 크기, 손실 또는 모델 신뢰도의 간단한 차이로 설명되지 않는다는 것입니다. 우리의 논문은 모델이 획득 시간에 따라 정보를 구별할 수 있는 능력을 보여주며, 모순되는 데이터를 어떻게 처리하고 지식 수정에 대응할지에 대한 중요한 함의를 가지고 있습니다.

## 📝 요약

이 연구는 언어 모델의 활성화가 훈련 중 언제 정보를 배웠는지 선형적으로 인코딩된다는 것을 보여줍니다. 실험에서는 Llama-3.2-1B를 순차적으로 fine-tuning하여 알려진 훈련 순서를 가진 모델을 만들었습니다. 테스트 샘플의 평균 활성화는 훈련 순서를 인코딩하며, 2D 부분 공간으로 투영하면 훈련 순서대로 정렬되고 직선상에 위치합니다. 또한 선형 프로브를 사용하여 "일찍" vs. "늦게" 학습된 엔티티를 정확하게 (~90%) 구별할 수 있음을 보여줍니다. 이러한 시간 신호는 간단한 활성화 크기, 손실 또는 모델 신뢰도의 차이로 설명되지 않습니다. 이 연구는 모델이 정보를 습득한 시간에 따라 구분할 수 있음을 보여주며, 모순되는 데이터를 어떻게 처리하고 지식 수정에 대응할지에 대한 중요한 함의를 가지고 있습니다.

## 🎯 주요 포인트


- 언어 모델의 활성화는 훈련 중에 언제 정보가 학습되었는지 선형적으로 인코딩됨을 보여줌

- 선형 프로브는 "일찍" 대 "늦게" 엔티티를 정확하게 (~90%) 구별할 수 있음

- 모델은 보고되지 않은 엔티티의 훈련 단계를 명시적으로 보고할 수 있음 (~80% 정확도)


---

*Generated on 2025-09-18 16:26:09*