# VOX-KRIKRI: Unifying Speech and Language through Continuous Fusion

**Korean Title:** VOX-KRIKRI: 연속 융합을 통한 음성과 언어의 통합

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Cross-modal Attention|Cross-modal Attention]] [[keywords/specific/Multimodal Fusion|Multimodal Fusion]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Automatic Speech Recognition|Automatic Speech Recognition]] [[keywords/unique/VoxKrikri|VoxKrikri]] [[categories/cs.CL|cs.CL]] [[2025-09-22/Speech Language Models for Under-Represented Languages_ Insights from Wolof_20250922|Speech Language Models for Under-Represented Languages: Insights from Wolof]] (81.3% similar) [[2025-09-22/Think, Verbalize, then Speak_ Bridging Complex Thoughts and Comprehensible Speech_20250922|Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech]] (80.8% similar) [[2025-09-19/Cross-Modal Knowledge Distillation for Speech Large Language Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Cross-modal Attention, Multimodal Fusion
**🔬 Broad Technical**: Large Language Models, Automatic Speech Recognition
**⭐ Unique Technical**: VoxKrikri
## 🔗 유사한 논문
- [[2025-09-22/Speech Language Models for Under-Represented Languages_ Insights from Wolof_20250922|Speech Language Models for Under-Represented Languages Insights from Wolof]] (81.3% similar)
- [[2025-09-22/Think, Verbalize, then Speak_ Bridging Complex Thoughts and Comprehensible Speech_20250922|Think, Verbalize, then Speak Bridging Complex Thoughts and Comprehensible Speech]] (80.8% similar)
- [[2025-09-19/Cross-Modal Knowledge Distillation for Speech Large Language Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (80.5% similar)
- [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (80.1% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony On Multilingual Data Allocation for Large Language Models Pretraining]] (79.8% similar)


**ArXiv ID**: [2509.15667](https://arxiv.org/abs/2509.15667)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15667.pdf)


**ArXiv ID**: [2509.15667](https://arxiv.org/abs/2509.15667)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15667.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Cross-modal Attention, Multimodal Fusion
**⭐ Unique Technical**: VoxKrikri
**🔬 Broad Technical**: Large Language Models, Automatic Speech Recognition

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Automatic Speech Recognition` • 

`Cross-modal Attention` • 

`Multimodal Fusion` • 

`VoxKrikri`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15667v1 Announce Type: new 
Abstract: We present a multimodal fusion framework that bridges pre-trained decoder-based large language models (LLM) and acoustic encoder-decoder architectures such as Whisper, with the aim of building speech-enabled LLMs. Instead of directly using audio embeddings, we explore an intermediate audio-conditioned text space as a more effective mechanism for alignment. Our method operates fully in continuous text representation spaces, fusing Whisper's hidden decoder states with those of an LLM through cross-modal attention, and supports both offline and streaming modes. We introduce \textit{VoxKrikri}, the first Greek speech LLM, and show through analysis that our approach effectively aligns representations across modalities. These results highlight continuous space fusion as a promising path for multilingual and low-resource speech LLMs, while achieving state-of-the-art results for Automatic Speech Recognition in Greek, providing an average $\sim20\%$ relative improvement across benchmarks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15667v1 발표 유형: 신규  
초록: 우리는 사전 훈련된 디코더 기반 대형 언어 모델(LLM)과 Whisper와 같은 음향 인코더-디코더 아키텍처를 연결하여 음성 지원 LLM을 구축하기 위한 다중 모달 융합 프레임워크를 제시합니다. 오디오 임베딩을 직접 사용하는 대신, 우리는 정렬을 위한 보다 효과적인 메커니즘으로서 중간 오디오 조건부 텍스트 공간을 탐색합니다. 우리의 방법은 Whisper의 숨겨진 디코더 상태를 LLM의 상태와 교차 모달 주의를 통해 융합하여, 연속적인 텍스트 표현 공간에서 완전히 작동하며 오프라인 및 스트리밍 모드를 모두 지원합니다. 우리는 첫 번째 그리스어 음성 LLM인 \textit{VoxKrikri}를 소개하고, 분석을 통해 우리의 접근 방식이 모달리티 간 표현을 효과적으로 정렬함을 보여줍니다. 이러한 결과는 연속 공간 융합이 다국어 및 저자원 음성 LLM을 위한 유망한 경로임을 강조하며, 그리스어 자동 음성 인식에서 벤치마크 전반에 걸쳐 평균 약 20%의 상대적 개선을 제공하면서 최첨단 결과를 달성합니다.

## 📝 요약

이 논문은 사전 학습된 디코더 기반 대형 언어 모델(LLM)과 Whisper와 같은 음성 인코더-디코더 아키텍처를 연결하는 다중 모달 융합 프레임워크를 제안합니다. 오디오 임베딩을 직접 사용하는 대신, 오디오 조건부 텍스트 공간을 활용하여 더 효과적인 정렬 메커니즘을 탐구합니다. 이 방법은 Whisper의 숨겨진 디코더 상태와 LLM의 상태를 교차 모달 주의 메커니즘으로 융합하여 연속적인 텍스트 표현 공간에서 작동하며, 오프라인 및 스트리밍 모드를 지원합니다. 이 연구에서는 첫 번째 그리스어 음성 LLM인 \textit{VoxKrikri}를 소개하고, 제안된 방법이 모달리티 간 표현을 효과적으로 정렬함을 보여줍니다. 이 결과는 연속 공간 융합이 다국어 및 저자원 음성 LLM에 유망한 경로임을 강조하며, 그리스어 자동 음성 인식에서 최첨단 결과를 달성하여 벤치마크에서 평균 약 20%의 상대적 향상을 제공합니다.

## 🎯 주요 포인트


- 1. 본 연구는 Whisper와 같은 음성 인코더-디코더 아키텍처와 사전 학습된 디코더 기반 대형 언어 모델(LLM)을 연결하는 다중 모달 융합 프레임워크를 제안합니다.

- 2. 오디오 임베딩을 직접 사용하는 대신, 중간 오디오 조건부 텍스트 공간을 활용하여 더 효과적인 정렬 메커니즘을 탐구합니다.

- 3. Whisper의 숨겨진 디코더 상태와 LLM의 상태를 교차 모달 주의를 통해 융합하여 연속적인 텍스트 표현 공간에서 작동하며, 오프라인 및 스트리밍 모드를 모두 지원합니다.

- 4. 그리스어 음성 LLM인 \textit{VoxKrikri}를 소개하며, 제안된 방법이 모달리티 간 표현을 효과적으로 정렬함을 분석을 통해 입증합니다.

- 5. 본 접근법은 그리스어 자동 음성 인식에서 최첨단 결과를 달성하며, 벤치마크 전반에 걸쳐 평균 약 20%의 상대적 개선을 제공합니다.


---

*Generated on 2025-09-22 16:25:45*