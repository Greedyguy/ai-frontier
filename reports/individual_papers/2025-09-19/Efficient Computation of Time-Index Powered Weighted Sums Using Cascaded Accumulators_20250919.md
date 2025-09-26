---
keywords:
  - Cascaded Accumulators
  - Time-Index Powered Weighted Sums
  - Real-Time Implementation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15069
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:47:02.954119",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cascaded Accumulators",
    "Time-Index Powered Weighted Sums",
    "Real-Time Implementation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Cascaded Accumulators": 0.78,
    "Time-Index Powered Weighted Sums": 0.72,
    "Real-Time Implementation": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Efficient Computation of Time-Index Powered Weighted Sums Using Cascaded Accumulators

**Korean Title:** 시간 지수 가중 합의 효율적인 계산을 위한 계단식 누산기 사용

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Real-Time Implementation|real-time implementation]]
**⚡ Unique Technical**: [[keywords/Cascaded Accumulators|cascaded accumulators]], [[keywords/Time-Index Powered Weighted Sums|time-index powered weighted sums]]

## 🔗 유사한 논문
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (77.2% similar)
- [[Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (77.0% similar)
- [[MaRVIn A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (75.8% similar)
- [[Catalpa GC for a Low-Variance Software Stack]] (75.2% similar)
- [[Streaming periodicity with mismatches, wildcards, and edits_20250919|Streaming periodicity with mismatches, wildcards, and edits]] (74.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15069v1 Announce Type: cross 
Abstract: This letter presents a novel approach for \mbox{efficiently} computing time-index powered weighted sums of the form $\sum_{n=0}^{N-1} n^{K} v[n]$ using cascaded accumulators. Traditional direct computation requires $K{\times}N$ general multiplications, which become prohibitive for large $N$, while alternative strategies based on lookup tables or signal reversal require storing entire data blocks. By exploiting accumulator properties, the proposed method eliminates the need for such storage and reduces the multiplicative cost to only $K{+}1$ constant multiplications, enabling efficient real-time implementation. The approach is particularly useful when such sums need to be efficiently computed in sample-by-sample processing systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.15069v1 발표 유형: 교차  
초록: 이 편지는 계단식 누산기를 사용하여 $\sum_{n=0}^{N-1} n^{K} v[n]$ 형태의 시간 인덱스 제곱 가중 합을 효율적으로 계산하기 위한 새로운 접근법을 제시합니다. 전통적인 직접 계산은 $K{\times}N$ 일반 곱셈을 필요로 하며, 이는 큰 $N$에 대해 부담이 됩니다. 반면에 조회 테이블이나 신호 반전을 기반으로 한 대체 전략은 전체 데이터 블록을 저장해야 합니다. 누산기의 특성을 활용함으로써 제안된 방법은 이러한 저장의 필요성을 제거하고 곱셈 비용을 $K{+}1$ 상수 곱셈으로 줄여, 실시간 구현을 가능하게 합니다. 이 접근법은 샘플별 처리 시스템에서 이러한 합을 효율적으로 계산해야 할 때 특히 유용합니다.

## 📝 요약

이 논문은 시간 인덱스가 있는 가중 합계를 효율적으로 계산하기 위한 새로운 방법을 제안합니다. 전통적인 방법은 많은 곱셈 연산을 필요로 하지만, 제안된 방법은 누산기의 특성을 활용하여 저장 공간 없이 곱셈 연산을 크게 줄입니다. 이 방법은 실시간 처리 시스템에서 샘플별로 이러한 합계를 효율적으로 계산할 수 있도록 하며, 특히 $K{+}1$의 상수 곱셈만으로 구현할 수 있어 실시간 처리에 유리합니다.

## 🎯 주요 포인트

- 1. 새로운 접근법은 누산기의 특성을 활용하여 시간 지수 가중 합을 효율적으로 계산합니다.

- 2. 제안된 방법은 $K{\times}N$ 일반 곱셈을 $K{+}1$ 상수 곱셈으로 줄여줍니다.

- 3. 데이터 블록 저장이 필요 없으며 실시간 구현에 적합합니다.

- 4. 샘플별 처리 시스템에서 효율적인 계산이 가능합니다.

---

*Generated on 2025-09-19 16:24:48*