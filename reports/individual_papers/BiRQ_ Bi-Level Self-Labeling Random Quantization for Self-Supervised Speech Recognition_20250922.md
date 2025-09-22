# BiRQ: Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition

**Korean Title:** BiRQ: 자가 지도 음성 인식을 위한 이중 수준 자기 레이블링 랜덤 양자화

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Random Quantization|Random Quantization]] [[keywords/specific/Bilevel Optimization|Bilevel Optimization]] [[keywords/broad/Self-supervised Learning|Self-supervised Learning]] [[keywords/unique/BiRQ|BiRQ]] [[categories/cs.CL|cs.CL]] [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (80.6% similar) [[2025-09-18/Evolving Language Models without Labels_ Majority Drives Selection, Novelty Promotes Variation_20250918|Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation]] (80.4% similar) [[2025-09-18/BabyHuBERT_ Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings_20250918|BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Self-labeling Random Quantization
**🔗 Specific Connectable**: First-order Bilevel Optimization
**🔬 Broad Technical**: Self-supervised Learning
**⭐ Unique Technical**: BiRQ
## 🔗 유사한 논문
- [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (80.6% similar)
- [[2025-09-18/Evolving Language Models without Labels_ Majority Drives Selection, Novelty Promotes Variation_20250918|Evolving Language Models without Labels Majority Drives Selection, Novelty Promotes Variation]] (80.4% similar)
- [[2025-09-18/BabyHuBERT_ Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings_20250918|BabyHuBERT Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings]] (80.2% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (80.1% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility Process-Supervised Rewrite for RAG]] (79.6% similar)


**ArXiv ID**: [2509.15430](https://arxiv.org/abs/2509.15430)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15430.pdf)


**ArXiv ID**: [2509.15430](https://arxiv.org/abs/2509.15430)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15430.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Self-labeling Random Quantization
**🔗 Specific Connectable**: Bilevel Optimization
**⭐ Unique Technical**: BiRQ
**🔬 Broad Technical**: Self-supervised Learning

## 🏷️ 추출된 키워드



`Self-supervised Learning` • 

`Bilevel Optimization` • 

`BiRQ` • 

`Random Quantization`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15430v1 Announce Type: new 
Abstract: Speech is a rich signal, and labeled audio-text pairs are costly, making self-supervised learning essential for scalable representation learning. A core challenge in speech SSL is generating pseudo-labels that are both informative and efficient: strong labels, such as those used in HuBERT, improve downstream performance but rely on external encoders and multi-stage pipelines, while efficient methods like BEST-RQ achieve simplicity at the cost of weaker labels. We propose BiRQ, a bilevel SSL framework that combines the efficiency of BEST-RQ with the refinement benefits of HuBERT-style label enhancement. The key idea is to reuse part of the model itself as a pseudo-label generator: intermediate representations are discretized by a random-projection quantizer to produce enhanced labels, while anchoring labels derived directly from the raw input stabilize training and prevent collapse. Training is formulated as an efficient first-order bilevel optimization problem, solved end-to-end with differentiable Gumbel-softmax selection. This design eliminates the need for external label encoders, reduces memory cost, and enables iterative label refinement in an end-to-end fashion. BiRQ consistently improves over BEST-RQ while maintaining low complexity and computational efficiency. We validate our method on various datasets, including 960-hour LibriSpeech, 150-hour AMI meetings and 5,000-hour YODAS, demonstrating consistent gains over BEST-RQ.

## 🔍 Abstract (한글 번역)

arXiv:2509.15430v1 발표 유형: 새로운 것  
초록: 음성은 풍부한 신호이며, 라벨이 있는 오디오-텍스트 쌍은 비용이 많이 들기 때문에 확장 가능한 표현 학습을 위해 자가 지도 학습(self-supervised learning)이 필수적입니다. 음성 SSL의 핵심 과제는 정보가 풍부하고 효율적인 의사 라벨(pseudo-label)을 생성하는 것입니다. HuBERT에서 사용되는 강력한 라벨은 다운스트림 성능을 향상시키지만 외부 인코더와 다단계 파이프라인에 의존하는 반면, BEST-RQ와 같은 효율적인 방법은 단순성을 얻는 대신 약한 라벨을 사용합니다. 우리는 BiRQ라는 이중 수준 SSL 프레임워크를 제안하여 BEST-RQ의 효율성과 HuBERT 스타일 라벨 개선의 정제 이점을 결합합니다. 핵심 아이디어는 모델의 일부를 의사 라벨 생성기로 재사용하는 것입니다: 중간 표현은 랜덤 프로젝션 양자화기를 통해 이산화되어 개선된 라벨을 생성하며, 원시 입력에서 직접 파생된 앵커 라벨은 훈련을 안정화하고 붕괴를 방지합니다. 훈련은 효율적인 1차 이중 수준 최적화 문제로 공식화되며, 차별 가능한 Gumbel-softmax 선택을 통해 종단 간으로 해결됩니다. 이 설계는 외부 라벨 인코더의 필요성을 제거하고 메모리 비용을 줄이며, 종단 간 방식으로 반복적인 라벨 개선을 가능하게 합니다. BiRQ는 BEST-RQ에 비해 낮은 복잡성과 계산 효율성을 유지하면서 일관되게 성능을 향상시킵니다. 우리는 960시간의 LibriSpeech, 150시간의 AMI 회의, 5,000시간의 YODAS를 포함한 다양한 데이터셋에서 우리의 방법을 검증하여 BEST-RQ에 비해 일관된 성능 향상을 입증합니다.

## 📝 요약

BiRQ는 음성 자기지도 학습(SSL)에서 효율성과 성능을 동시에 개선하는 새로운 프레임워크입니다. 기존의 HuBERT는 강력한 레이블을 사용해 성능을 높이지만 복잡한 외부 인코더와 다단계 파이프라인이 필요합니다. 반면 BEST-RQ는 단순하지만 약한 레이블을 사용합니다. BiRQ는 모델의 일부를 의사 레이블 생성기로 활용하여 중간 표현을 무작위 투영 양자화기로 변환하고, 원시 입력에서 직접 파생된 앵커 레이블로 훈련을 안정화합니다. 이 방법은 외부 레이블 인코더 없이 메모리 비용을 줄이고, 차별 가능한 Gumbel-softmax 선택을 통해 효율적인 일차 최적화 문제로 훈련을 진행합니다. 다양한 데이터셋에서 BiRQ는 BEST-RQ보다 일관되게 성능을 향상시키며, 낮은 복잡성과 계산 효율성을 유지합니다.

## 🎯 주요 포인트


- 1. BiRQ는 BEST-RQ의 효율성과 HuBERT 스타일의 라벨 향상 이점을 결합한 이중 레벨 자가 지도 학습 프레임워크입니다.

- 2. 모델의 일부를 의사 라벨 생성기로 재사용하여 중간 표현을 무작위 투영 양자화기로 이산화하여 향상된 라벨을 생성합니다.

- 3. Gumbel-softmax 선택을 사용한 효율적인 1차 이중 레벨 최적화 문제로 훈련이 공식화되어 외부 라벨 인코더가 필요하지 않습니다.

- 4. BiRQ는 BEST-RQ에 비해 일관되게 성능을 향상시키면서도 낮은 복잡성과 계산 효율성을 유지합니다.

- 5. 다양한 데이터셋에서 BiRQ의 성능을 검증하여 BEST-RQ 대비 일관된 성능 향상을 입증했습니다.


---

*Generated on 2025-09-22 16:21:13*