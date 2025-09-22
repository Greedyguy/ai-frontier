# Aligning Audio Captions with Human Preferences

**Korean Title:** 오디오 캡션을 인간의 선호도에 맞추기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Kartik Hegde|Kartik Hegde]] [[authors/Rehana Mahfuz|Rehana Mahfuz]] [[authors/Yinyi Guo|Yinyi Guo]] [[authors/Erik Visser|Erik Visser]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Reinforcement Learning from Human Feedback

## 🔗 유사한 논문
- [[Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (82.6% similar)
- [[Listening, Imagining & Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining & Refining A Heuristic Optimized ASR Correction Framework with LLMs]] (78.2% similar)
- [[Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (78.0% similar)
- [[ToolSample_ Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning_20250919|ToolSample Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning]] (77.9% similar)
- [[RLBind_ Adversarial-Invariant Cross-Modal Alignment for Unified Robust Embeddings_20250919|RLBind Adversarial-Invariant Cross-Modal Alignment for Unified Robust Embeddings]] (77.6% similar)

## 📋 저자 정보

**Authors:** Kartik Hegde, Rehana Mahfuz, Yinyi Guo, Erik Visser

## 📄 Abstract (원문)

Current audio captioning systems rely heavily on supervised learning with
paired audio-caption datasets, which are expensive to curate and may not
reflect human preferences in real-world scenarios. To address this limitation,
we propose a preference-aligned audio captioning framework based on
Reinforcement Learning from Human Feedback (RLHF). To effectively capture
nuanced human preferences, we train a Contrastive Language-Audio Pretraining
(CLAP)-based reward model using human-labeled pairwise preference data. This
reward model is integrated into a reinforcement learning framework to fine-tune
any baseline captioning system without relying on ground-truth caption
annotations. Extensive human evaluations across multiple datasets show that our
method produces captions preferred over those from baseline models,
particularly in cases where the baseline models fail to provide correct and
natural captions. Furthermore, our framework achieves performance comparable to
supervised approaches with ground-truth data, demonstrating its effectiveness
in aligning audio captioning with human preferences and its scalability in
real-world scenarios.

## 🔍 Abstract (한글 번역)

현재의 오디오 캡셔닝 시스템은 고비용의 오디오-캡션 데이터셋을 사용한 지도 학습에 크게 의존하고 있으며, 이는 현실 세계의 시나리오에서 인간의 선호를 반영하지 못할 수 있습니다. 이러한 한계를 해결하기 위해, 우리는 인간 피드백 기반 강화 학습(RLHF)을 바탕으로 한 선호 정렬 오디오 캡셔닝 프레임워크를 제안합니다. 인간의 미묘한 선호를 효과적으로 포착하기 위해, 우리는 인간이 라벨링한 쌍별 선호 데이터로 대조 언어-오디오 사전학습(CLAP) 기반 보상 모델을 훈련합니다. 이 보상 모델은 강화 학습 프레임워크에 통합되어, 실제 캡션 주석에 의존하지 않고도 어떤 기본 캡셔닝 시스템을 미세 조정할 수 있습니다. 여러 데이터셋에 걸친 광범위한 인간 평가 결과, 우리의 방법은 특히 기본 모델이 정확하고 자연스러운 캡션을 제공하지 못하는 경우에 기본 모델보다 선호되는 캡션을 생성하는 것으로 나타났습니다. 또한, 우리의 프레임워크는 실제 데이터가 있는 지도 학습 접근법과 비교할 만한 성능을 달성하여, 오디오 캡셔닝을 인간의 선호와 정렬시키는 데 있어 그 효과성을 입증하며, 현실 세계 시나리오에서의 확장 가능성을 보여줍니다.

## 📝 요약

본 논문에서는 기존의 오디오 캡셔닝 시스템이 고비용의 데이터셋에 의존하고 현실의 인간 선호도를 반영하지 못하는 문제를 해결하기 위해, 인간 피드백을 활용한 강화 학습(RLHF)을 기반으로 하는 선호도 정렬 오디오 캡셔닝 프레임워크를 제안합니다. 인간이 라벨링한 쌍별 선호 데이터로 CLAP 기반 보상 모델을 훈련하여 미세한 인간 선호도를 효과적으로 포착합니다. 이 보상 모델은 강화 학습 프레임워크에 통합되어, 실제 캡션 주석 없이도 기존 캡셔닝 시스템을 미세 조정할 수 있습니다. 여러 데이터셋에 대한 광범위한 인간 평가 결과, 제안된 방법이 기존 모델보다 선호되는 캡션을 생성하며, 특히 기존 모델이 정확하고 자연스러운 캡션을 제공하지 못하는 경우에 두드러집니다. 또한, 제안된 프레임워크는 실제 데이터 기반의 지도 학습 접근법과 유사한 성능을 보여, 인간 선호도와의 정렬 및 현실적 확장 가능성을 입증합니다.

## 🎯 주요 포인트

- 1. 기존의 오디오 캡셔닝 시스템은 고비용의 오디오-캡션 데이터셋에 의존하며, 실제 상황에서 인간의 선호를 반영하지 못하는 한계가 있다.

- 2. 제안된 프레임워크는 인간 피드백을 활용한 강화 학습(RLHF)을 기반으로 하여, 인간의 미묘한 선호를 효과적으로 포착하기 위해 CLAP 기반 보상 모델을 훈련한다.

- 3. 보상 모델은 강화 학습 프레임워크에 통합되어, 실제 캡션 주석 없이도 기본 캡셔닝 시스템을 미세 조정할 수 있다.

- 4. 다양한 데이터셋에서의 인간 평가 결과, 제안된 방법이 기본 모델보다 선호되는 캡션을 생성하며, 특히 기본 모델이 정확하고 자연스러운 캡션을 제공하지 못하는 경우에 효과적이다.

- 5. 제안된 프레임워크는 실제 데이터와 비교 가능한 성능을 보여주며, 인간 선호에 맞춘 오디오 캡셔닝의 효과성과 실제 시나리오에서의 확장성을 입증한다.

---

*Generated on 2025-09-20 05:46:18*