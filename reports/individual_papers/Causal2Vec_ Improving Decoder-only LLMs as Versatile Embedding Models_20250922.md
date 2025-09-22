# Causal2Vec: Improving Decoder-only LLMs as Versatile Embedding Models

**Korean Title:** Causal2Vec: 디코더 전용 LLM을 다용도 임베딩 모델로 개선하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Bidirectional Attention, Semantic Information Encoding

## 🔗 유사한 논문
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text]] (83.4% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.7% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (81.8% similar)
- [[2025-09-19/VLM-E2E_ Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion_20250919|VLM-E2E Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion]] (81.8% similar)
- [[2025-09-18/TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.23386v2 Announce Type: replace-cross 
Abstract: Decoder-only large language models (LLMs) are increasingly used to build embedding models that effectively encode the semantic information of natural language texts into dense vector representations for various embedding tasks. However, many existing methods primarily focus on removing the causal attention mask in LLMs to enable bidirectional attention, potentially undermining the model's ability to extract semantic information acquired during pretraining. Additionally, leading unidirectional approaches often rely on extra input text to overcome the inherent limitations of causal attention, inevitably increasing computational costs. In this work, we propose Causal2Vec, a general-purpose embedding model tailored to enhance the performance of decoder-only LLMs without altering their original architectures or introducing significant computational overhead. Specifically, we first employ a lightweight BERT-style model to pre-encode the input text into a single Contextual token, which is then prepended to the LLM's input sequence, allowing each token to capture contextualized information even without attending to future tokens. Furthermore, to mitigate the recency bias introduced by last-token pooling and help LLMs better leverage the semantic information encoded in the Contextual token, we concatenate the last hidden states of Contextual and EOS tokens as the final text embedding. In practice, Causal2Vec achieves state-of-the-art performance on the Massive Text Embeddings Benchmark (MTEB) among models trained solely on publicly available retrieval datasets, while reducing the required sequence length by up to 85% and inference time by up to 82% compared to best-performing methods.

## 🔍 Abstract (한글 번역)

arXiv:2507.23386v2 발표 유형: 교차 교체  
초록: 디코더 전용 대형 언어 모델(LLMs)은 자연어 텍스트의 의미 정보를 다양한 임베딩 작업을 위해 밀집 벡터 표현으로 효과적으로 인코딩하는 임베딩 모델을 구축하는 데 점점 더 많이 사용되고 있습니다. 그러나 많은 기존 방법들은 LLM에서 인과적 주의 마스크를 제거하여 양방향 주의를 가능하게 하는 데 주로 초점을 맞추고 있으며, 이는 사전 학습 중에 획득한 의미 정보를 추출하는 모델의 능력을 잠재적으로 저해할 수 있습니다. 또한, 주요 단방향 접근법은 종종 인과적 주의의 고유한 한계를 극복하기 위해 추가 입력 텍스트에 의존하며, 이는 필연적으로 계산 비용을 증가시킵니다. 이 연구에서는 디코더 전용 LLM의 원래 아키텍처를 변경하거나 상당한 계산 오버헤드를 도입하지 않고 성능을 향상시키기 위해 설계된 범용 임베딩 모델인 Causal2Vec을 제안합니다. 구체적으로, 우리는 먼저 경량의 BERT 스타일 모델을 사용하여 입력 텍스트를 단일 컨텍스추얼 토큰으로 사전 인코딩하고, 이를 LLM의 입력 시퀀스에 앞에 배치하여 각 토큰이 미래 토큰에 주의를 기울이지 않고도 컨텍스트화된 정보를 캡처할 수 있도록 합니다. 또한, 마지막 토큰 풀링에 의해 도입된 최신 편향을 완화하고 LLM이 컨텍스추얼 토큰에 인코딩된 의미 정보를 더 잘 활용할 수 있도록, 컨텍스추얼 및 EOS 토큰의 마지막 은닉 상태를 최종 텍스트 임베딩으로 연결합니다. 실제로, Causal2Vec은 공개적으로 사용 가능한 검색 데이터셋에서만 훈련된 모델 중에서 대규모 텍스트 임베딩 벤치마크(MTEB)에서 최첨단 성능을 달성하며, 최상의 성능을 보이는 방법에 비해 필요한 시퀀스 길이를 최대 85%, 추론 시간을 최대 82%까지 줄입니다.

## 📝 요약

Causal2Vec는 디코더 전용 대형 언어 모델(LLM)의 성능을 향상시키기 위한 일반적인 임베딩 모델로, 기존 아키텍처를 변경하거나 계산 비용을 크게 증가시키지 않습니다. 이 모델은 경량의 BERT 스타일 모델을 사용하여 입력 텍스트를 사전 인코딩한 후, 이를 LLM 입력 시퀀스에 추가하여 각 토큰이 미래 토큰을 참조하지 않고도 문맥 정보를 캡처할 수 있게 합니다. 또한, 마지막 토큰 풀링의 편향을 줄이고 문맥 토큰의 의미 정보를 더 잘 활용하기 위해 마지막 숨겨진 상태를 결합하여 최종 텍스트 임베딩을 생성합니다. Causal2Vec는 공개된 데이터셋만으로 훈련된 모델 중 최고 성능을 기록하며, 시퀀스 길이를 최대 85%, 추론 시간을 최대 82%까지 줄였습니다.

## 🎯 주요 포인트

- 1. Causal2Vec는 디코더 전용 대형 언어 모델(LLMs)의 성능을 향상시키기 위해 설계된 범용 임베딩 모델로, 기존 아키텍처를 변경하거나 계산 비용을 크게 증가시키지 않습니다.

- 2. 이 모델은 입력 텍스트를 사전 인코딩하기 위해 경량의 BERT 스타일 모델을 사용하여, 각 토큰이 미래의 토큰에 주의를 기울이지 않고도 문맥화된 정보를 캡처할 수 있도록 합니다.

- 3. Causal2Vec는 마지막 토큰 풀링에 의한 최신성 편향을 완화하고, 문맥화된 토큰에 인코딩된 의미 정보를 더 잘 활용하기 위해 마지막 숨겨진 상태를 최종 텍스트 임베딩으로 사용합니다.

- 4. 이 모델은 공개된 검색 데이터셋으로만 학습된 모델 중에서 Massive Text Embeddings Benchmark (MTEB)에서 최첨단 성능을 달성하며, 최적의 성능을 보이는 방법들과 비교하여 시퀀스 길이를 최대 85%, 추론 시간을 최대 82%까지 줄입니다.

---

*Generated on 2025-09-22 14:57:40*