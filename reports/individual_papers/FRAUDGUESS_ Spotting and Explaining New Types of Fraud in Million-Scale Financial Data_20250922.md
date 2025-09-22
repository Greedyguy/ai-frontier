# FRAUDGUESS: Spotting and Explaining New Types of Fraud in Million-Scale Financial Data

**Korean Title:** FRAUDGUESS: 백만 규모의 금융 데이터에서 새로운 유형의 사기를 식별하고 설명하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interactive Dashboard for Fraud Detection

## 🔗 유사한 논문
- [[2025-09-19/Evaluating Supervised Learning Models for Fraud Detection_ A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data_20250919|Evaluating Supervised Learning Models for Fraud Detection A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data]] (82.8% similar)
- [[2025-09-17/Synthesizing Behaviorally-Grounded Reasoning Chains_ A Data-Generation Framework for Personal Finance LLMs_20250917|Synthesizing Behaviorally-Grounded Reasoning Chains A Data-Generation Framework for Personal Finance LLMs]] (77.4% similar)
- [[2025-09-18/From Patterns to Predictions_ A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets_20250918|From Patterns to Predictions A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets]] (77.3% similar)
- [[2025-09-18/Credit Card Fraud Detection_20250918|Credit Card Fraud Detection]] (77.2% similar)
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (76.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15493v1 Announce Type: new 
Abstract: Given a set of financial transactions (who buys from whom, when, and for how much), as well as prior information from buyers and sellers, how can we find fraudulent transactions? If we have labels for some transactions for known types of fraud, we can build a classifier. However, we also want to find new types of fraud, still unknown to the domain experts ('Detection'). Moreover, we also want to provide evidence to experts that supports our opinion ('Justification'). In this paper, we propose FRAUDGUESS, to achieve two goals: (a) for 'Detection', it spots new types of fraud as micro-clusters in a carefully designed feature space; (b) for 'Justification', it uses visualization and heatmaps for evidence, as well as an interactive dashboard for deep dives. FRAUDGUESS is used in real life and is currently considered for deployment in an Anonymous Financial Institution (AFI). Thus, we also present the three new behaviors that FRAUDGUESS discovered in a real, million-scale financial dataset. Two of these behaviors are deemed fraudulent or suspicious by domain experts, catching hundreds of fraudulent transactions that would otherwise go un-noticed.

## 🔍 Abstract (한글 번역)

arXiv:2509.15493v1 발표 유형: 신규  
초록: 금융 거래 집합(누가 누구에게 언제 얼마에 구매하는지)과 구매자 및 판매자의 사전 정보를 주어졌을 때, 어떻게 하면 사기 거래를 찾아낼 수 있을까요? 일부 거래에 대해 알려진 사기 유형의 라벨이 있다면, 우리는 분류기를 구축할 수 있습니다. 그러나 우리는 또한 도메인 전문가에게 아직 알려지지 않은 새로운 유형의 사기를 발견하고자 합니다('탐지'). 게다가, 우리는 우리의 의견을 뒷받침하는 증거를 전문가에게 제공하고자 합니다('정당화'). 본 논문에서는 두 가지 목표를 달성하기 위해 FRAUDGUESS를 제안합니다: (a) '탐지'를 위해, 신중하게 설계된 특징 공간에서 미세 클러스터로 새로운 유형의 사기를 포착합니다; (b) '정당화'를 위해, 증거로 시각화 및 히트맵을 사용하고, 심층 분석을 위한 대화형 대시보드를 활용합니다. FRAUDGUESS는 실제로 사용되고 있으며, 현재 익명의 금융 기관(AFI)에서 배포를 고려 중입니다. 따라서 우리는 실제 백만 규모의 금융 데이터셋에서 FRAUDGUESS가 발견한 세 가지 새로운 행동을 제시합니다. 이 중 두 가지 행동은 도메인 전문가에 의해 사기 또는 의심스러운 것으로 간주되며, 그렇지 않으면 눈에 띄지 않았을 수백 건의 사기 거래를 포착합니다.

## 📝 요약

이 논문에서는 금융 거래 데이터를 분석하여 새로운 유형의 사기 거래를 탐지하고 이를 전문가에게 설명할 수 있는 FRAUDGUESS라는 시스템을 제안합니다. FRAUDGUESS는 두 가지 주요 목표를 달성합니다. 첫째, '탐지' 측면에서, 정교하게 설계된 특징 공간에서 미세 군집을 찾아 새로운 사기 유형을 발견합니다. 둘째, '정당화' 측면에서, 시각화와 히트맵을 사용하여 증거를 제공하고, 심층 분석을 위한 대화형 대시보드를 제공합니다. 이 시스템은 실제 금융 데이터에 적용되어 세 가지 새로운 행동 패턴을 발견했으며, 그 중 두 가지는 전문가에 의해 사기성 또는 의심스러운 것으로 판단되었습니다. 이를 통해 수백 건의 사기 거래를 추가로 탐지할 수 있었습니다. FRAUDGUESS는 현재 익명의 금융 기관에서 도입을 고려 중입니다.

## 🎯 주요 포인트

- 1. FRAUDGUESS는 새로운 유형의 사기를 탐지하기 위해 정교하게 설계된 특징 공간에서 미세 클러스터를 식별합니다.

- 2. FRAUDGUESS는 시각화 및 히트맵을 사용하여 전문가에게 사기 탐지에 대한 증거를 제공하며, 심층 분석을 위한 대화형 대시보드를 제공합니다.

- 3. FRAUDGUESS는 실제 금융 데이터셋에서 세 가지 새로운 행동 패턴을 발견했으며, 이 중 두 가지는 전문가들에 의해 사기 또는 의심스러운 것으로 간주되었습니다.

- 4. FRAUDGUESS는 수백 건의 사기 거래를 탐지하여, 그렇지 않으면 간과될 수 있는 거래들을 포착했습니다.

- 5. FRAUDGUESS는 익명의 금융 기관에서 실제로 사용되고 있으며, 배포가 고려되고 있습니다.

---

*Generated on 2025-09-22 15:15:53*