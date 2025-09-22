# cadrille: Multi-modal CAD Reconstruction with Online Reinforcement Learning

**Korean Title:** 카드릴: 온라인 강화 학습을 통한 다중 모드 CAD 재구성

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Online Reinforcement Learning|Online Reinforcement Learning]] [[keywords/specific/Multi-modal CAD Reconstruction|Multi-modal CAD Reconstruction]] [[keywords/broad/Reinforcement Learning|Reinforcement Learning]] [[keywords/broad/Vision Language Models|Vision Language Models]] [[keywords/unique/cadrille|cadrille]] [[categories/cs.LG|cs.LG]] [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (85.3% similar) [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (82.6% similar) [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Online Reinforcement Learning
**🔗 Specific Connectable**: Multi-modal CAD Reconstruction
**🔬 Broad Technical**: Reinforcement Learning, Vision Language Models
**⭐ Unique Technical**: cadrille
## 🔗 유사한 논문
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (85.3% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1 Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (82.6% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.2% similar)
- [[2025-09-19/Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (82.2% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.8% similar)


**ArXiv ID**: [2505.22914](https://arxiv.org/abs/2505.22914)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2505.22914.pdf)


**ArXiv ID**: [2505.22914](https://arxiv.org/abs/2505.22914)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2505.22914.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Online Reinforcement Learning
**🔗 Specific Connectable**: Multi-modal CAD Reconstruction
**⭐ Unique Technical**: cadrille
**🔬 Broad Technical**: Reinforcement Learning, Vision Language Models

## 🏷️ 추출된 키워드



`Reinforcement Learning` • 

`Vision Language Models` • 

`Multi-modal CAD Reconstruction` • 

`cadrille` • 

`Online Reinforcement Learning`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22914v2 Announce Type: replace-cross 
Abstract: Computer-Aided Design (CAD) plays a central role in engineering and manufacturing, making it possible to create precise and editable 3D models. Using a variety of sensor or user-provided data as inputs for CAD reconstruction can democratize access to design applications. However, existing methods typically focus on a single input modality, such as point clouds, images, or text, which limits their generalizability and robustness. Leveraging recent advances in vision-language models (VLM), we propose a multi-modal CAD reconstruction model that simultaneously processes all three input modalities. Inspired by large language model (LLM) training paradigms, we adopt a two-stage pipeline: supervised fine-tuning (SFT) on large-scale procedurally generated data, followed by reinforcement learning (RL) fine-tuning using online feedback, obtained programatically. Furthermore, we are the first to explore RL fine-tuning of LLMs for CAD tasks demonstrating that online RL algorithms such as Group Relative Preference Optimization (GRPO) outperform offline alternatives. In the DeepCAD benchmark, our SFT model outperforms existing single-modal approaches in all three input modalities simultaneously. More importantly, after RL fine-tuning, cadrille sets new state-of-the-art on three challenging datasets, including a real-world one.

## 🔍 Abstract (한글 번역)

arXiv:2505.22914v2 발표 유형: 교차 교체  
초록: 컴퓨터 지원 설계(CAD)는 공학 및 제조 분야에서 중심적인 역할을 하며, 정밀하고 편집 가능한 3D 모델을 생성할 수 있게 해줍니다. 다양한 센서 또는 사용자 제공 데이터를 CAD 재구성의 입력으로 사용하면 설계 애플리케이션에 대한 접근을 민주화할 수 있습니다. 그러나 기존 방법들은 일반적으로 포인트 클라우드, 이미지 또는 텍스트와 같은 단일 입력 모달리티에 집중하여, 이들의 일반화 가능성과 견고성을 제한합니다. 최근의 비전-언어 모델(VLM) 발전을 활용하여, 우리는 세 가지 입력 모달리티를 동시에 처리하는 다중 모달 CAD 재구성 모델을 제안합니다. 대형 언어 모델(LLM) 훈련 패러다임에서 영감을 받아, 우리는 대규모 절차적으로 생성된 데이터에 대한 지도 학습(SFT)과 온라인 피드백을 통해 프로그램적으로 얻은 강화 학습(RL) 미세 조정을 포함하는 두 단계 파이프라인을 채택합니다. 더욱이, 우리는 CAD 작업을 위한 LLM의 RL 미세 조정을 탐구한 최초의 연구로서, Group Relative Preference Optimization (GRPO)와 같은 온라인 RL 알고리즘이 오프라인 대안보다 뛰어나다는 것을 입증합니다. DeepCAD 벤치마크에서, 우리의 SFT 모델은 세 가지 입력 모달리티 모두에서 기존의 단일 모달 접근 방식을 능가합니다. 더 중요한 것은, RL 미세 조정 후, cadrille은 실제 데이터를 포함한 세 가지 도전적인 데이터셋에서 새로운 최첨단 성능을 설정합니다.

## 📝 요약

이 논문은 CAD(컴퓨터 지원 설계) 재구성을 위한 다중 모달 모델을 제안합니다. 기존 방법들이 단일 입력 모달리티에 집중하는 한계를 극복하기 위해, 이 모델은 점 구름, 이미지, 텍스트 등 세 가지 입력 모달리티를 동시에 처리합니다. 대규모 언어 모델(LLM) 훈련 방식을 참고하여, 대규모 절차적으로 생성된 데이터에 대한 지도 학습(SFT)과 온라인 피드백을 활용한 강화 학습(RL) 미세 조정을 수행합니다. 특히, CAD 작업에 LLM의 RL 미세 조정을 처음으로 탐구하며, 온라인 RL 알고리즘인 GRPO가 오프라인 대안을 능가함을 보여줍니다. DeepCAD 벤치마크에서 제안된 모델은 세 가지 입력 모달리티 모두에서 기존 단일 모달 접근법을 능가하며, RL 미세 조정 후에는 세 가지 도전적인 데이터셋에서 최신 성능을 기록합니다.

## 🎯 주요 포인트


- 1. CAD 재구성 모델은 다양한 센서 및 사용자 제공 데이터를 입력으로 사용하여 디자인 애플리케이션 접근성을 향상시킬 수 있습니다.

- 2. 기존 방법들은 단일 입력 모달리티에 집중하지만, 제안된 모델은 포인트 클라우드, 이미지, 텍스트를 동시에 처리하는 멀티모달 접근 방식을 채택합니다.

- 3. 대규모 언어 모델(LLM) 훈련 패러다임에서 영감을 받아, 대규모 절차적으로 생성된 데이터에 대한 감독된 미세 조정(SFT)과 온라인 피드백을 통한 강화 학습(RL) 미세 조정의 두 단계 파이프라인을 사용합니다.

- 4. CAD 작업을 위한 LLM의 RL 미세 조정을 탐구한 최초의 연구로, 온라인 RL 알고리즘인 Group Relative Preference Optimization (GRPO)이 오프라인 대안을 능가함을 보여줍니다.

- 5. DeepCAD 벤치마크에서 제안된 SFT 모델은 모든 세 가지 입력 모달리티에서 기존 단일 모달 접근 방식을 능가하며, RL 미세 조정 후에는 세 가지 도전적인 데이터셋에서 새로운 최첨단 성능을 달성합니다.


---

*Generated on 2025-09-22 16:11:34*