# Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery

**Korean Title:** 약물 발견을 위한 세밀한 결합 표현을 활용한 구조 인식 대조 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Jing Lan|Jing Lan]] [[authors/Hexiao Ding|Hexiao Ding]] [[authors/Hongzhao Chen|Hongzhao Chen]] [[authors/Yufeng Jiang|Yufeng Jiang]] [[authors/Nga-Chun Ng|Nga-Chun Ng]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Attention Mechanism, Virtual Screening

## 🔗 유사한 논문
- [[(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (79.2% similar)
- [[Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (78.6% similar)
- [[Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (78.5% similar)
- [[Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (78.3% similar)
- [[Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2 Atypical Mitosis Classification]] (78.2% similar)

## 📋 저자 정보

**Authors:** Jing Lan, Hexiao Ding, Hongzhao Chen, Yufeng Jiang, Nga-Chun Ng, Gwing Kei Yip, Gerald W. Y. Cheng, Yunlin Mao, Jing Cai, Liang-ting Lin, Jung Sun Yoo

## 📄 Abstract (원문)

Accurate identification of drug-target interactions (DTI) remains a central
challenge in computational pharmacology, where sequence-based methods offer
scalability. This work introduces a sequence-based drug-target interaction
framework that integrates structural priors into protein representations while
maintaining high-throughput screening capability. Evaluated across multiple
benchmarks, the model achieves state-of-the-art performance on Human and
BioSNAP datasets and remains competitive on BindingDB. In virtual screening
tasks, it surpasses prior methods on LIT-PCBA, yielding substantial gains in
AUROC and BEDROC. Ablation studies confirm the critical role of learned
aggregation, bilinear attention, and contrastive alignment in enhancing
predictive robustness. Embedding visualizations reveal improved spatial
correspondence with known binding pockets and highlight interpretable attention
patterns over ligand-residue contacts. These results validate the framework's
utility for scalable and structure-aware DTI prediction.

## 🔍 Abstract (한글 번역)

약물-표적 상호작용(DTI)의 정확한 식별은 계산 약리학에서 여전히 중심적인 과제이며, 서열 기반 방법은 확장성을 제공합니다. 본 연구는 서열 기반 약물-표적 상호작용 프레임워크를 소개하며, 이는 단백질 표현에 구조적 사전 지식을 통합하면서도 고처리량 스크리닝 능력을 유지합니다. 여러 벤치마크를 통해 평가된 이 모델은 Human 및 BioSNAP 데이터셋에서 최첨단 성능을 달성하고, BindingDB에서도 경쟁력을 유지합니다. 가상 스크리닝 작업에서 LIT-PCBA에 대한 이전 방법을 능가하며, AUROC 및 BEDROC에서 상당한 향상을 이끌어냅니다. 소거 연구는 학습된 집계, 이중선형 주의, 대조적 정렬이 예측의 견고성을 향상시키는 데 중요한 역할을 한다는 것을 확인합니다. 임베딩 시각화는 알려진 결합 포켓과의 공간적 대응이 개선되었음을 보여주고, 리간드-잔기 접촉에 대한 해석 가능한 주의 패턴을 강조합니다. 이러한 결과는 확장 가능하고 구조를 인식하는 DTI 예측을 위한 프레임워크의 유용성을 검증합니다.

## 📝 요약

이 연구는 약물-표적 상호작용(DTI)의 정확한 식별을 위한 시퀀스 기반 프레임워크를 제안하며, 단백질 표현에 구조적 사전 지식을 통합하여 대량 스크리닝 기능을 유지합니다. Human 및 BioSNAP 데이터셋에서 최첨단 성능을 보였으며, BindingDB에서도 경쟁력을 유지합니다. 가상 스크리닝 작업에서는 LIT-PCBA에서 이전 방법을 능가하여 AUROC와 BEDROC에서 상당한 향상을 보였습니다. 소거 연구는 학습된 집계, 이중선형 주의, 대조 정렬이 예측 강건성을 높이는 데 중요함을 확인했습니다. 임베딩 시각화는 알려진 결합 포켓과의 공간적 대응을 개선하고 리간드-잔기 접촉에 대한 해석 가능한 주의 패턴을 강조합니다. 이 결과는 확장 가능하고 구조를 고려한 DTI 예측에 대한 프레임워크의 유용성을 입증합니다.

## 🎯 주요 포인트

- 1. 본 연구는 구조적 정보를 통합한 서열 기반 약물-표적 상호작용 프레임워크를 제안하여 높은 처리량의 스크리닝 기능을 유지합니다.

- 2. 제안된 모델은 Human 및 BioSNAP 데이터셋에서 최첨단 성능을 달성하고, BindingDB에서도 경쟁력을 유지합니다.

- 3. 가상 스크리닝 작업에서 LIT-PCBA 데이터셋에 대해 이전 방법들을 능가하며 AUROC 및 BEDROC에서 상당한 향상을 보입니다.

- 4. 소거 연구는 학습된 집계, 이중 선형 주의 메커니즘, 대조 정렬이 예측의 견고성을 향상시키는 데 중요한 역할을 한다는 것을 확인합니다.

- 5. 임베딩 시각화는 알려진 결합 포켓과의 공간적 대응을 개선하고 리간드-잔기 접촉에 대한 해석 가능한 주의 패턴을 강조합니다.

---

*Generated on 2025-09-20 02:50:24*