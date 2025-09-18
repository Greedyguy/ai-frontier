
# Towards Unified and Adaptive Cross-Domain Collaborative Filtering via Graph Signal Processing

**Korean Title:** 그래프 신호 처리를 통한 통합 및 적응형 교차 도메인 협업 필터링으로 나아가기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Intra-domain Recommendations|Intra-domain Recommendations]] [[keywords/broad/Collaborative Filtering|Collaborative Filtering]] [[keywords/broad/Cross-Domain Recommendation|Cross-Domain Recommendation]] [[keywords/specific/Graph Filtering|Graph Filtering]] [[keywords/unique/CGSP|CGSP]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Intra-domain Recommendations
**🔬 Broad Technical**: Collaborative Filtering, Cross-Domain Recommendation
**🔗 Specific Connectable**: Graph Filtering
**⭐ Unique Technical**: CGSP

**ArXiv ID**: [2407.12374](https://arxiv.org/abs/2407.12374)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2407.12374.pdf)


## 🏷️ 추출된 키워드



`Collaborative Filtering` • 

`Cross-Domain Recommendation` • 

`Graph Filtering` • 

`CGSP` • 

`Intra-domain Recommendations`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.12374v3 Announce Type: replace-cross 
Abstract: Collaborative Filtering (CF) is a foundational approach in recommender systems, but it struggles with challenges such as data sparsity and the cold-start problem. Cross-Domain Recommendation (CDR) has emerged as a promising solution by leveraging dense domains to improve recommendations in sparse target domains. However, existing CDR methods face significant limitations, including their reliance on overlapping users as a bridge between domains and their inability to address domain sensitivity, i.e., differences in user behaviors and characteristics across domains, effectively. To overcome these limitations, we propose CGSP, a unified and adaptive CDR framework based on graph signal processing (GSP). CGSP supports both intra-domain and inter-domain recommendations while adaptively controlling the influence of the source domain through a simple hyperparameter. The framework constructs a cross-domain similarity graph by integrating target-only and source-bridged similarity graphs to capture both intra-domain and inter-domain relationships. This graph is then processed through graph filtering techniques to propagate and enhance local signals. Finally, personalized graph signals are constructed, tailored separately for users in the source and target domains, enabling CGSP to function as a unified framework for CDR scenarios. Extensive evaluation shows that CGSP outperforms state-of-the-art baselines across diverse cross-domain settings, with notable gains in low-overlap scenarios, underscoring its practicality for real-world applications.

## 🔍 Abstract (한글 번역)

arXiv:2407.12374v3 발표 유형: replace-cross
요약: 협업 필터링(CF)은 추천 시스템에서의 기본적인 접근 방식이지만, 데이터 희소성과 콜드 스타트 문제와 같은 어려움을 겪고 있습니다. Cross-Domain Recommendation (CDR)은 밀도가 높은 도메인을 활용하여 희소한 대상 도메인에서 추천을 개선하는 유망한 해결책으로 등장했습니다. 그러나 기존의 CDR 방법은 도메인 간의 다양한 사용자를 연결하는 다리로서의 중복 사용자에 의존하고 도메인 감도성, 즉 도메인 간의 사용자 행동 및 특성의 차이를 효과적으로 다루지 못하는 등의 중요한 제한 사항이 있습니다. 이러한 제한 사항을 극복하기 위해, 우리는 그래프 신호 처리(GSP)를 기반으로 한 통합적이고 적응적인 CDR 프레임워크인 CGSP를 제안합니다. CGSP는 단순한 하이퍼파라미터를 통해 소스 도메인의 영향을 적응적으로 제어하면서 도메인 내 및 도메인 간 추천을 지원합니다. 이 프레임워크는 대상 도메인 전용 및 소스를 통해 연결된 유사도 그래프를 통합하여 도메인 내 및 도메인 간 관계를 포착합니다. 이 그래프는 그래프 필터링 기술을 통해 처리되어 지역 신호를 전파하고 강화합니다. 마지막으로, 소스 및 대상 도메인의 사용자에 대해 개인화된 그래프 신호가 구성되어 CGSP가 CDR 시나리오에 대한 통합 프레임워크로 작동할 수 있도록 합니다. 광범위한 평가 결과, CGSP가 다양한 크로스 도메인 설정에서 최첨단 기준선을 능가하며, 특히 저 중복 시나리오에서 현저한 향상을 보여주어 실제 응용 프로그램에 대한 실용성을 강조합니다.

## 📝 요약

협업 필터링은 추천 시스템에서 중요한 방법론이지만 데이터 희소성과 콜드 스타트 문제와 같은 어려움을 겪고 있다. 이에 교차 도메인 추천은 밀도가 높은 도메인을 활용하여 희소한 대상 도메인에서 추천을 개선하는 유망한 해결책으로 등장했다. 그러나 기존의 교차 도메인 추천 방법은 중요한 한계점을 가지고 있었는데, 이는 도메인 간의 중첩 사용자에 의존하고 도메인 감도성, 즉 도메인 간 사용자 행동 및 특성의 차이를 효과적으로 다루지 못한다는 것이다. 이러한 한계를 극복하기 위해 우리는 그래프 신호 처리(GSP)를 기반으로 한 통합적이고 적응적인 교차 도메인 추천 프레임워크인 CGSP를 제안한다. CGSP는 소스 도메인의 영향을 간단한 하이퍼파라미터를 통해 조절하면서 도메인 내 및 도메인 간 추천을 지원한다. 이 프레임워크는 대상 전용 및 소스-교차 유사도 그래프를 통합하여 도메인 내 및 도메인 간 관계를 포착하는 교차 도메인 유사도 그래프를 구성한다. 이 그래프는 그래프 필터링 기술을 통해 처리되어 지역 신호를 전파하고 강화한다. 마지막으로, 소스 및 대상 도메인의 사용자에 맞게 개인화된 그래프 신호가 구성되어 CGSP가 교차 도메인 추천 시나리오에 대한 통합 프레임워크로 작동할 수 있게 한다. 광범위한 평가 결과, CGSP가 다양한 교차 도메인 설정에서 최첨단 기준선을 능가하며, 낮은 중첩 시나리오에서 현저한 향상을 보여 실세계 응용에 대한 실용성을 강조한다.

## 🎯 주요 포인트


- 협업 필터링은 추천 시스템에서 중요한 방법론이지만 데이터 희소성과 콜드 스타트 문제와 같은 어려움을 겪고 있다.

- Cross-Domain Recommendation (CDR)은 밀집 도메인을 활용하여 희소한 대상 도메인에서 추천을 개선하는 유망한 해결책으로 등장했다.

- 기존 CDR 방법론은 중요한 한계점을 가지고 있으며, 이를 극복하기 위해 CGSP를 제안한다.

- CGSP는 그래프 신호 처리를 기반으로 한 통합적이고 적응적인 CDR 프레임워크로, 다양한 교차 도메인 설정에서 최신 기준선을 능가하는 것으로 나타났다.


---

*Generated on 2025-09-18 16:28:50*