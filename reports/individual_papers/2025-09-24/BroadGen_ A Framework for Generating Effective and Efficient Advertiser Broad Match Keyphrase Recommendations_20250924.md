<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:34:44.126137",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Broad Match Keyphrases",
    "Token Correspondence Modeling",
    "Search Query Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Broad Match Keyphrases": 0.78,
    "Token Correspondence Modeling": 0.75,
    "Search Query Data": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Broad match keyphrases",
        "canonical": "Broad Match Keyphrases",
        "aliases": [
          "Broad match",
          "Broad keyphrases"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and provides a unique technical concept for linking in the context of search advertising.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Token correspondence modeling",
        "canonical": "Token Correspondence Modeling",
        "aliases": [
          "Token modeling",
          "Correspondence modeling"
        ],
        "category": "unique_technical",
        "rationale": "This term describes a specific technique used in the framework, offering a unique perspective for linking related research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Historical search query data",
        "canonical": "Search Query Data",
        "aliases": [
          "Historical search data",
          "Query data"
        ],
        "category": "broad_technical",
        "rationale": "This term is essential for understanding the data-driven approach of the framework and links to data usage in advertising.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "exact match types",
      "management expenses",
      "targeting scope"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Broad match keyphrases",
      "resolved_canonical": "Broad Match Keyphrases",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Token correspondence modeling",
      "resolved_canonical": "Token Correspondence Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Historical search query data",
      "resolved_canonical": "Search Query Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# BroadGen: A Framework for Generating Effective and Efficient Advertiser Broad Match Keyphrase Recommendations

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.19164.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2505.19164](https://arxiv.org/abs/2505.19164)

## 🔗 유사한 논문
- [[2025-09-22/Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search_20250922|Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search]] (80.6% similar)
- [[2025-09-23/SeqUDA-Rec_ Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation for Personalized Content Marketing_20250923|SeqUDA-Rec: Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation for Personalized Content Marketing]] (79.9% similar)
- [[2025-09-22/Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings_20250922|Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings]] (79.4% similar)
- [[2025-09-18/GEM-Bench_ A Benchmark for Ad-Injected Response Generation within Generative Engine Marketing_20250918|GEM-Bench: A Benchmark for Ad-Injected Response Generation within Generative Engine Marketing]] (79.4% similar)
- [[2025-09-19/JU-NLP at Touch\'e_ Covert Advertisement in Conversational AI-Generation and Detection Strategies_20250919|JU-NLP at Touch\'e: Covert Advertisement in Conversational AI-Generation and Detection Strategies]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Search Query Data|Search Query Data]]
**⚡ Unique Technical**: [[keywords/Broad Match Keyphrases|Broad Match Keyphrases]], [[keywords/Token Correspondence Modeling|Token Correspondence Modeling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.19164v3 Announce Type: replace-cross 
Abstract: In the domain of sponsored search advertising, the focus of {Keyphrase recommendation has largely been on exact match types, which pose issues such as high management expenses, limited targeting scope, and evolving search query patterns. Alternatives like Broad match types can alleviate certain drawbacks of exact matches but present challenges like poor targeting accuracy and minimal supervisory signals owing to limited advertiser usage. This research defines the criteria for an ideal broad match, emphasizing on both efficiency and effectiveness, ensuring that a significant portion of matched queries are relevant. We propose BroadGen, an innovative framework that recommends efficient and effective broad match keyphrases by utilizing historical search query data. Additionally, we demonstrate that BroadGen, through token correspondence modeling, maintains better query stability over time. BroadGen's capabilities allow it to serve daily, millions of sellers at eBay with over 2.5 billion items.

## 📝 요약

이 연구는 스폰서 검색 광고에서 키프레이즈 추천의 문제점을 해결하기 위해 Broad match 유형의 개선된 방법론인 BroadGen을 제안합니다. 기존의 정확한 매치 방식은 관리 비용이 높고 타겟 범위가 제한적이며, 검색 쿼리 패턴 변화에 대응하기 어렵습니다. Broad match는 이러한 문제를 완화할 수 있지만, 타겟 정확도가 낮고 광고주 사용이 적어 감독 신호가 부족합니다. BroadGen은 효율성과 효과성을 동시에 고려하여 관련성이 높은 쿼리를 매칭하는 이상적인 Broad match 기준을 정의하고, 과거 검색 쿼리 데이터를 활용하여 효과적인 키프레이즈를 추천합니다. 또한, BroadGen은 토큰 대응 모델링을 통해 시간에 따른 쿼리 안정성을 유지하며, eBay의 수백만 판매자와 25억 개 이상의 아이템을 지원할 수 있는 능력을 입증합니다.

## 🎯 주요 포인트

- 1. 기존의 정확한 일치 유형은 높은 관리 비용과 제한된 타겟 범위 등의 문제를 야기합니다.
- 2. Broad match 유형은 정확한 일치의 단점을 완화할 수 있지만, 타겟 정확도와 광고주 사용의 한계로 인한 감독 신호 부족 등의 문제를 겪습니다.
- 3. BroadGen은 효율적이고 효과적인 broad match 키프레이즈를 추천하는 혁신적인 프레임워크로, 역사적 검색 쿼리 데이터를 활용합니다.
- 4. BroadGen은 토큰 대응 모델링을 통해 시간이 지나도 더 나은 쿼리 안정성을 유지합니다.
- 5. BroadGen은 eBay의 수백만 명의 판매자에게 매일 25억 개 이상의 아이템을 제공할 수 있는 능력을 갖추고 있습니다.


---

*Generated on 2025-09-24 14:34:44*