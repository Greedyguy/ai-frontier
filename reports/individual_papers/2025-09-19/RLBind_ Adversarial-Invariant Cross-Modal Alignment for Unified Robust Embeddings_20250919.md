
# RLBind: Adversarial-Invariant Cross-Modal Alignment for Unified Robust Embeddings

**Korean Title:** RLBind: 통합된 강건한 임베딩을 위한 적대적 불변 교차 모달 정렬

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adversarial-invariant Embeddings

## 🔗 유사한 논문
- [[Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (80.5% similar)
- [[Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (80.1% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (79.9% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (79.9% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (79.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14383v1 Announce Type: cross 
Abstract: Unified multi-modal encoders that bind vision, audio, and other sensors into a shared embedding space are attractive building blocks for robot perception and decision-making. However, on-robot deployment exposes the vision branch to adversarial and natural corruptions, making robustness a prerequisite for safety. Prior defenses typically align clean and adversarial features within CLIP-style encoders and overlook broader cross-modal correspondence, yielding modest gains and often degrading zero-shot transfer. We introduce RLBind, a two-stage adversarial-invariant cross-modal alignment framework for robust unified embeddings. Stage 1 performs unsupervised fine-tuning on clean-adversarial pairs to harden the visual encoder. Stage 2 leverages cross-modal correspondence by minimizing the discrepancy between clean/adversarial features and a text anchor, while enforcing class-wise distributional alignment across modalities. Extensive experiments on Image, Audio, Thermal, and Video data show that RLBind consistently outperforms the LanguageBind backbone and standard fine-tuning baselines in both clean accuracy and norm-bounded adversarial robustness. By improving resilience without sacrificing generalization, RLBind provides a practical path toward safer multi-sensor perception stacks for embodied robots in navigation, manipulation, and other autonomy settings.

## 🔍 Abstract (한글 번역)

arXiv:2509.14383v1 발표 유형: 교차  
초록: 시각, 오디오 및 기타 센서를 공유 임베딩 공간으로 결합하는 통합 멀티모달 인코더는 로봇의 인식 및 의사 결정에 매력적인 구성 요소입니다. 그러나 로봇에 배치하면 시각 분기가 적대적 및 자연적 손상에 노출되어 안전을 위한 강건성이 필수적입니다. 이전 방어 기법은 일반적으로 CLIP 스타일 인코더 내에서 깨끗한 기능과 적대적 기능을 정렬하고 더 넓은 교차 모달 대응을 간과하여 미미한 향상을 가져오고 종종 제로샷 전이를 저하시킵니다. 우리는 강력한 통합 임베딩을 위한 두 단계의 적대적 불변 교차 모달 정렬 프레임워크인 RLBind를 소개합니다. 1단계는 시각 인코더를 강화하기 위해 깨끗한-적대적 쌍에 대한 비지도 세부 조정을 수행합니다. 2단계는 텍스트 앵커와의 깨끗한/적대적 기능 간의 불일치를 최소화하고 모달리티 간의 클래스별 분포 정렬을 강제하여 교차 모달 대응을 활용합니다. 이미지, 오디오, 열화상 및 비디오 데이터에 대한 광범위한 실험을 통해 RLBind는 깨끗한 정확도와 노름 제한 적대적 강건성 모두에서 LanguageBind 백본 및 표준 세부 조정 기준선을 일관되게 능가함을 보여줍니다. 일반화를 희생하지 않고 회복력을 향상시킴으로써 RLBind는 탐색, 조작 및 기타 자율성 설정에서 구현된 로봇을 위한 보다 안전한 다중 센서 인식 스택을 위한 실용적인 경로를 제공합니다.

## 📝 요약

이 논문은 로봇의 인식 및 의사결정에 사용되는 통합 멀티모달 인코더의 강건성을 향상시키기 위한 새로운 프레임워크 RLBind를 제안합니다. RLBind는 두 단계로 구성된 적대적 불변 교차 모달 정렬 방법론을 통해 시각 인코더의 강건성을 강화합니다. 첫 번째 단계에서는 깨끗한 데이터와 적대적 데이터 쌍을 사용하여 비지도 학습을 수행하고, 두 번째 단계에서는 텍스트 앵커와의 불일치를 최소화하여 모달 간의 클래스별 분포 정렬을 강화합니다. 실험 결과, RLBind는 다양한 데이터 유형에서 기존 방법보다 높은 정확성과 강건성을 보여주며, 로봇의 안전한 멀티센서 인식에 기여할 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. RLBind는 비전, 오디오 등 다양한 센서를 통합하여 로봇의 인식 및 의사결정에 활용할 수 있는 통합 멀티모달 인코더를 제안합니다.

- 2. RLBind는 두 단계의 적대적-불변 크로스모달 정렬 프레임워크로, 시각 인코더의 강건성을 강화하기 위해 클린-적대적 쌍에 대한 비지도 미세 조정을 수행합니다.

- 3. RLBind는 텍스트 앵커와의 불일치를 최소화하고, 모달리티 간 클래스별 분포 정렬을 통해 크로스모달 대응을 활용합니다.

- 4. RLBind는 이미지, 오디오, 열화상, 비디오 데이터에 대한 실험에서 LanguageBind 백본 및 표준 미세 조정 기법보다 우수한 성능을 보였습니다.

- 5. RLBind는 일반화 능력을 희생하지 않으면서 강건성을 개선하여 로봇의 내비게이션, 조작 등 자율성 환경에서 안전한 멀티센서 인식 스택을 제공합니다.

---

*Generated on 2025-09-19 16:12:19*