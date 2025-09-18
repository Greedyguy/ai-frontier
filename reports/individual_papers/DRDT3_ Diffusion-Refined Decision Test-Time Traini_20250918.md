
# DRDT3: Diffusion-Refined Decision Test-Time Training Model

**Korean Title:** DRDT3: 확산-정제된 의사결정 테스트 시간 훈련 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Diffusion-Refined Decision|Diffusion-Refined Decision]] [[keywords/broad/Recurrent Neural Networks|Recurrent Neural Networks]] [[keywords/broad/Test-Time Training|Test-Time Training]] [[keywords/specific/Trajectory Modelling|Trajectory Modelling]] [[keywords/unique/DRDT3|DRDT3]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Trajectory Modelling
**🔬 Broad Technical**: Decision Transformer, Recurrent Neural Networks
**🔗 Specific Connectable**: Generative Modelling
**⭐ Unique Technical**: Diffusion-Refined Decision TTT (DRDT3

**ArXiv ID**: [2501.06718](https://arxiv.org/abs/2501.06718)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2501.06718.pdf)


## 🏷️ 추출된 키워드



`Decision Transformer` • 

`Recurrent Neural Networks` • 

`Trajectory Modelling` • 

`Diffusion-Refined Decision TTT (DRDT3` • 

`Generative Diffusion Model`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.06718v2 Announce Type: replace 
Abstract: Decision Transformer (DT), a trajectory modelling method, has shown competitive performance compared to traditional offline reinforcement learning (RL) approaches on various classic control tasks. However, it struggles to learn optimal policies from suboptimal, reward-labelled trajectories. In this study, we explore the use of conditional generative modelling to facilitate trajectory stitching given its high-quality data generation ability. Additionally, recent advancements in Recurrent Neural Networks (RNNs) have shown their linear complexity and competitive sequence modelling performance over Transformers. We leverage the Test-Time Training (TTT) layer, an RNN that updates hidden states during testing, to model trajectories in the form of DT. We introduce a unified framework, called Diffusion-Refined Decision TTT (DRDT3), to achieve performance beyond DT models. Specifically, we propose the Decision TTT (DT3) module, which harnesses the sequence modelling strengths of both self-attention and the TTT layer to capture recent contextual information and make coarse action predictions. DRDT3 iteratively refines the coarse action predictions through the generative diffusion model, progressively moving closer to the optimal actions. We further integrate DT3 with the diffusion model using a unified optimization objective. With experiments on multiple tasks in the D4RL benchmark, our DT3 model without diffusion refinement demonstrates improved performance over standard DT, while DRDT3 further achieves superior results compared to state-of-the-art DT-based and offline RL methods.

## 🔍 Abstract (한글 번역)

arXiv:2501.06718v2 발표 유형: 대체
요약: 결정 트랜스포머(DT)는 전통적인 오프라인 강화 학습(RL) 접근법과 비교하여 다양한 클래식 제어 작업에서 경쟁력 있는 성능을 보여주는 궤적 모델링 방법입니다. 그러나, DT는 부적절한 보상이 라벨링된 궤적에서 최적 정책을 학습하는 데 어려움을 겪습니다. 본 연구에서는 고품질 데이터 생성 능력을 감안하여 조건부 생성 모델링의 사용을 탐구하여 궤적 스티칭을 용이하게 합니다. 또한, 최근의 순환 신경망(RNNs)의 발전은 선형 복잡성과 트랜스포머보다 우수한 순차 모델링 성능을 보여주었습니다. 우리는 테스트 시간 훈련(TTT) 레이어를 활용하여 DT 형태로 궤적을 모델링하는 RNN인 TTT 레이어를 사용합니다. 우리는 DT 모델을 뛰어넘는 성능을 달성하기 위해 DRDT3라는 통합된 프레임워크를 소개합니다. 구체적으로, 우리는 최근의 문맥 정보를 캡처하고 대략적인 행동 예측을 수행하기 위해 self-attention과 TTT 레이어의 순차 모델링 강점을 활용하는 Decision TTT (DT3) 모듈을 제안합니다. DRDT3는 생성 확산 모델을 통해 대략적인 행동 예측을 반복적으로 개선하여 최적의 행동에 점점 가까워집니다. 우리는 통합 최적화 목표를 사용하여 DT3를 확산 모델과 통합합니다. D4RL 벤치마크의 여러 작업에서의 실험을 통해, 확산 개선 없이 DT3 모델이 표준 DT보다 성능이 향상되었으며, DRDT3는 최첨단 DT 기반 및 오프라인 RL 방법과 비교하여 우수한 결과를 달성했습니다.

## 📝 요약

본 연구에서는 결정 트랜스포머(Decision Transformer, DT)를 통해 전통적인 오프라인 강화 학습 방법과 경쟁력 있는 성능을 보였으나, 부적절한 보상이 라벨링된 궤적에서 최적 정책을 학습하는 데 어려움이 있음을 밝혔다. 이에 우리는 조건부 생성 모델링을 활용하여 궤적 연결을 용이하게 하는 방법을 탐구했으며, 최근 발전된 순환 신경망(RNNs) 기술을 활용하여 DT 형태의 궤적을 모델링하기 위해 Test-Time Training (TTT) 레이어를 활용한 통합된 프레임워크인 DRDT3를 제안했다. 실험 결과, DRDT3는 기존 DT 모델 및 오프라인 RL 방법보다 우수한 성과를 보였다.

## 🎯 주요 포인트


- 1. Decision Transformer (DT)는 전통적인 오프라인 강화 학습 접근법에 비해 경쟁력 있는 성능을 보이지만, 부적절한 보상이 레이블된 궤적에서 최적 정책을 학습하는 데 어려움을 겪는다.

- 2. 최근 RNN의 선형 복잡성과 Transformer보다 우수한 시퀀스 모델링 성능을 활용하여 Test-Time Training (TTT) 레이어를 활용한 DT 모델인 DRDT3를 소개한다.

- 3. DRDT3는 DT 모델을 뛰어넘는 성능을 달성하며, 최적의 행동에 점진적으로 가까워지도록 생성 확산 모델을 통해 거친 행동 예측을 반복적으로 개선한다.


---

*Generated on 2025-09-18 16:46:20*