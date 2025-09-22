
# Value-Guided KV Compression for LLMs via Approximated CUR Decomposition

**Korean Title:** 가치 기반 KV 압축을 위한 LLM의 근사 CUR 분해 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Value Guided KV Compression

## 🔗 유사한 논문
- [[NIRVANA Structured pruning reimagined for large language models compression]] (81.3% similar)
- [[V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (80.6% similar)
- [[Communication Efficient Split Learning of ViTs with Attention-based Double Compression_20250919|Communication Efficient Split Learning of ViTs with Attention-based Double Compression]] (80.3% similar)
- [[Delta Knowledge Distillation for Large Language Models_20250919|Delta Knowledge Distillation for Large Language Models]] (79.5% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15038v1 Announce Type: new 
Abstract: Key-value (KV) cache compression has emerged as a critical technique for reducing the memory and latency overhead of autoregressive language models during inference. Prior approaches predominantly rely on query-key attention scores to rank and evict cached tokens, assuming that attention intensity correlates with semantic importance. However, this heuristic overlooks the contribution of value vectors, which directly influence the attention output. In this paper, we propose CurDKV, a novel, value-centric KV compression method that selects keys and values based on leverage scores computed from CUR matrix decomposition. Our approach approximates the dominant subspace of the attention output $softmax(QK^T)V$, ensuring that the retained tokens best preserve the model's predictive behavior. Theoretically, we show that attention score approximation does not guarantee output preservation, and demonstrate that CUR-based selection minimizes end-to-end attention reconstruction loss. Empirically, CurDKV achieves up to 9.6% higher accuracy than state-of-the-art methods like SnapKV and ChunkKV under aggressive compression budgets on LLaMA and Mistral, while maintaining compatibility with FlashAttention and Grouped Query Attention. In addition to improved accuracy, CurDKV reduces generation latency by up to 40% at high compression, offering a practical speed-accuracy tradeoff.

## 🔍 Abstract (한글 번역)

arXiv:2509.15038v1 발표 유형: 신규  
초록: 키-값(KV) 캐시 압축은 추론 중 자가회귀 언어 모델의 메모리 및 지연 오버헤드를 줄이기 위한 중요한 기술로 부상하고 있습니다. 이전 접근법들은 주로 쿼리-키 주의 점수를 사용하여 캐시된 토큰을 순위 매기고 제거하는데, 이는 주의 강도가 의미적 중요성과 상관관계가 있다고 가정합니다. 그러나 이 휴리스틱은 주의 출력에 직접적으로 영향을 미치는 값 벡터의 기여를 간과합니다. 본 논문에서는 CUR 행렬 분해에서 계산된 레버리지 점수를 기반으로 키와 값을 선택하는 새로운 값 중심의 KV 압축 방법인 CurDKV를 제안합니다. 우리의 접근법은 주의 출력 $softmax(QK^T)V$의 지배적인 부분 공간을 근사하여, 유지된 토큰이 모델의 예측 행동을 최적으로 보존하도록 합니다. 이론적으로, 우리는 주의 점수 근사가 출력 보존을 보장하지 않음을 보여주고, CUR 기반 선택이 종단 간 주의 재구성 손실을 최소화함을 입증합니다. 실험적으로, CurDKV는 LLaMA와 Mistral에서 공격적인 압축 예산 하에 SnapKV 및 ChunkKV와 같은 최신 방법들보다 최대 9.6% 높은 정확도를 달성하며, FlashAttention 및 Grouped Query Attention과의 호환성을 유지합니다. 향상된 정확도 외에도, CurDKV는 높은 압축에서 최대 40%의 생성 지연을 줄여 실용적인 속도-정확도 절충을 제공합니다.

## 📝 요약

이 논문에서는 자가회귀 언어 모델의 추론 시 메모리와 지연 시간을 줄이기 위한 새로운 키-값(KV) 캐시 압축 방법인 CurDKV를 제안합니다. 기존 방법은 주로 쿼리-키 주의 점수에 의존하여 캐시된 토큰을 관리했지만, 이는 값 벡터의 기여를 간과합니다. CurDKV는 CUR 행렬 분해를 통해 계산된 레버리지 점수를 기반으로 키와 값을 선택하여 주의 출력의 지배적 부분 공간을 근사합니다. 이 방법은 모델의 예측 성능을 최적화하며, 이론적으로 주의 점수 근사가 출력 보존을 보장하지 않음을 보여주고, CUR 기반 선택이 주의 재구성 손실을 최소화함을 입증합니다. 실험 결과, CurDKV는 LLaMA와 Mistral 모델에서 SnapKV 및 ChunkKV보다 최대 9.6% 높은 정확도를 달성하고, 생성 지연 시간을 최대 40% 줄여 실용적인 속도-정확도 균형을 제공합니다.

## 🎯 주요 포인트

- 1. CurDKV는 CUR 행렬 분해를 활용한 새로운 값 중심의 KV 압축 방법을 제안합니다.

- 2. 제안된 방법은 $softmax(QK^T)V$의 주도적인 부분 공간을 근사하여 모델의 예측 성능을 최적화합니다.

- 3. CUR 기반 선택은 주의 출력 보존을 보장하지 않는 기존 주의 점수 근사법보다 종단 간 주의 재구성 손실을 최소화합니다.

- 4. CurDKV는 LLaMA와 Mistral에서 SnapKV 및 ChunkKV보다 최대 9.6% 높은 정확도를 달성합니다.

- 5. 높은 압축률에서 CurDKV는 생성 지연을 최대 40% 줄이며, FlashAttention 및 Grouped Query Attention과의 호환성을 유지합니다.

---

*Generated on 2025-09-19 15:53:59*