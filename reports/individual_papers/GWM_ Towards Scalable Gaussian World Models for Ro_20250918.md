
# GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

**Korean Title:** GWM: 로봇 조작을 위한 확장 가능한 가우시안 월드 모델로의 진화

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Model-based Reinforcement Learning|Model-based Reinforcement Learning]] [[keywords/broad/Gaussian World Models|Gaussian World Models]] [[keywords/broad/Robotics|Robotics]] [[keywords/specific/Diffusion Transformer|Diffusion Transformer]] [[keywords/unique/Gaussian World Model (GWM|Gaussian World Model (GWM]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Model-based Reinforcement Learning
**🔬 Broad Technical**: Gaussian World Models, Robotics
**🔗 Specific Connectable**: Diffusion Transformer
**⭐ Unique Technical**: Gaussian World Model (GWM

**ArXiv ID**: [2508.17600](https://arxiv.org/abs/2508.17600)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2508.17600.pdf)


## 🏷️ 추출된 키워드



`Gaussian World Models` • 

`Robotics` • 

`Diffusion Transformer` • 

`Gaussian World Model (GWM` • 

`Model-based Reinforcement Learning`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.17600v2 Announce Type: replace-cross 
Abstract: Training robot policies within a learned world model is trending due to the inefficiency of real-world interactions. The established image-based world models and policies have shown prior success, but lack robust geometric information that requires consistent spatial and physical understanding of the three-dimensional world, even pre-trained on internet-scale video sources. To this end, we propose a novel branch of world model named Gaussian World Model (GWM) for robotic manipulation, which reconstructs the future state by inferring the propagation of Gaussian primitives under the effect of robot actions. At its core is a latent Diffusion Transformer (DiT) combined with a 3D variational autoencoder, enabling fine-grained scene-level future state reconstruction with Gaussian Splatting. GWM can not only enhance the visual representation for imitation learning agent by self-supervised future prediction training, but can serve as a neural simulator that supports model-based reinforcement learning. Both simulated and real-world experiments depict that GWM can precisely predict future scenes conditioned on diverse robot actions, and can be further utilized to train policies that outperform the state-of-the-art by impressive margins, showcasing the initial data scaling potential of 3D world model.

## 🔍 Abstract (한글 번역)

arXiv:2508.17600v2 발표 유형: 대체-교차
요약: 학습된 세계 모델 내에서 로봇 정책을 훈련시키는 것이 현실 세계 상호작용의 비효율성으로 인해 인기를 얻고 있습니다. 이미 구축된 이미지 기반 세계 모델과 정책은 이전에 성공을 거두었지만, 3차원 세계의 일관된 공간적 및 물리적 이해를 필요로 하는 견고한 기하학적 정보가 부족합니다. 심지어 인터넷 규모의 비디오 소스에서 사전 훈련된 상태에서도 그렇습니다. 이를 위해 로봇 조작을 위한 새로운 세계 모델 분야인 가우시안 세계 모델(GWM)을 제안합니다. 이 모델은 로봇 조작의 영향 하에 가우시안 원시의 전파를 추론하여 미래 상태를 재구성합니다. 핵심은 잠재 확산 변환기(DiT)와 3D 변이 오토인코더를 결합한 것으로, 가우시안 스플래팅을 통해 세밀한 장면 수준의 미래 상태 재구성이 가능합니다. GWM은 자기 지도 미래 예측 훈련을 통해 모방 학습 에이전트의 시각적 표현을 향상시킬 뿐만 아니라, 모델 기반 강화 학습을 지원하는 신경 시뮬레이터 역할을 할 수 있습니다. 시뮬레이션 및 현실 세계 실험 모두 GWM이 다양한 로봇 조작에 조건을 부여한 미래 장면을 정확하게 예측할 수 있으며, 최첨단 기술을 능가하는 정책을 훈련시키는 데 사용될 수 있음을 보여줍니다. 이는 3D 세계 모델의 초기 데이터 확장 잠재력을 보여주는 것입니다.

## 📝 요약

로봇 정책을 학습하는 데 있어 학습된 세계 모델 내에서의 훈련이 실제 상호작용의 비효율성으로 인해 트렌드로 떠오르고 있다. 기존의 이미지 기반 세계 모델과 정책은 성공을 거두었지만, 일관된 공간 및 물리적 이해를 필요로 하는 강건한 기하학적 정보가 부족하다. 이에 우리는 로봇 조작을 위한 새로운 세계 모델 분야인 가우시안 세계 모델(GWM)을 제안한다. GWM은 로봇 작업의 영향 하에 가우시안 기본체의 전파를 추론하여 미래 상태를 재구성한다. GWM은 미래 예측 훈련을 통해 시각적 표현을 향상시키고, 모델 기반 강화 학습을 지원하는 신경 시뮬레이터로 작용할 수 있다. 시뮬레이션 및 실제 실험 결과는 GWM이 다양한 로봇 작업에 조건을 걸어 미래 장면을 정확하게 예측하고, 최첨단 기술을 능가하는 정책을 훈련하는 데 활용될 수 있음을 보여주며, 3D 세계 모델의 초기 데이터 확장 잠재력을 보여준다.

## 🎯 주요 포인트


- 1. 로봇 정책을 학습하는 데에는 학습된 세계 모델 내에서 효율적이지 않은 실제 세계 상호작용 때문에 이미지 기반의 세계 모델과 정책이 성공을 거두었지만, 일정한 공간적 및 물리적 이해가 필요한 강건한 기하학적 정보가 부족하다.

- 2. Gaussian World Model (GWM)은 로봇 조작을 위한 새로운 세계 모델 분야로, 로봇 작용의 영향 하에 가우시안 원시체의 전파를 추론하여 미래 상태를 재구성한다.

- 3. GWM은 자기 지도 학습을 통해 시각적 표현을 향상시키고, 모델 기반 강화 학습을 지원하는 신경 시뮬레이터로 작용할 수 있으며, 다양한 로봇 작용에 조건을 두고 미래 장면을 정확하게 예측할 수 있다.


---

*Generated on 2025-09-18 16:34:14*