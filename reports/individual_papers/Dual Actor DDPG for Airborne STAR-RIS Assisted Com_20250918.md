
# Dual Actor DDPG for Airborne STAR-RIS Assisted Communications

**Korean Title:** 공중 STAR-RIS 지원 통신을 위한 이중 주체 DDPG

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Simultaneous Transmit and Reflect|Simultaneous Transmit and Reflect]] [[keywords/broad/Deep Deterministic Policy Gradient|Deep Deterministic Policy Gradient]] [[keywords/broad/Reconfigurable Intelligent Surface|Reconfigurable Intelligent Surface]] [[keywords/specific/Beamforming|Beamforming]] [[keywords/unique/Dual Actor DDPG|Dual Actor DDPG]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Simultaneous Transmit and Reflect
**🔬 Broad Technical**: Deep Deterministic Policy Gradient, Reconfigurable Intelligent Surface
**🔗 Specific Connectable**: UAV trajectory optimization
**⭐ Unique Technical**: Dual Actor DDPG

**ArXiv ID**: [2509.13328](https://arxiv.org/abs/2509.13328)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13328.pdf)


## 🏷️ 추출된 키워드



`Deep Deterministic Policy Gradient` • 

`Reconfigurable Intelligent Surface` • 

`UAV trajectory optimization` • 

`Dual Actor DDPG` • 

`Simultaneous Transmit and Reflect`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13328v1 Announce Type: cross 
Abstract: This study departs from the prevailing assumption of independent Transmission and Reflection Coefficients (TRC) in Airborne Simultaneous Transmit and Reflect Reconfigurable Intelligent Surface (STAR-RIS) research. Instead, we explore a novel multi-user downlink communication system that leverages a UAV-mounted STAR-RIS (Aerial-STAR) incorporating a coupled TRC phase shift model. Our key contributions include the joint optimization of UAV trajectory, active beamforming vectors at the base station, and passive RIS TRCs to enhance communication efficiency, while considering UAV energy constraints. We design the TRC as a combination of discrete and continuous actions, and propose a novel Dual Actor Deep Deterministic Policy Gradient (DA-DDPG) algorithm. The algorithm relies on two separate actor networks for high-dimensional hybrid action space. We also propose a novel harmonic mean index (HFI)-based reward function to ensure communication fairness amongst users. For comprehensive analysis, we study the impact of RIS size on UAV aerodynamics showing that it increases drag and energy demand. Simulation results demonstrate that the proposed DA-DDPG algorithm outperforms conventional DDPG and DQN-based solutions by 24% and 97%, respectively, in accumulated reward. Three-dimensional UAV trajectory optimization achieves 28% higher communication efficiency compared to two-dimensional and altitude optimization. The HFI based reward function provides 41% lower QoS denial rates as compared to other benchmarks. The mobile Aerial-STAR system shows superior performance over fixed deployed counterparts, with the coupled phase STAR-RIS outperforming dual Transmit/Reflect RIS and conventional RIS setups. These findings highlight the potential of Aerial-STAR systems and the effectiveness of our proposed DA-DDPG approach in optimizing their performance.

## 🔍 Abstract (한글 번역)

arXiv:2509.13328v1 발표 유형: 교차
요약: 본 연구는 대기 중복 송수신 재구성 지능 표면 (STAR-RIS) 연구에서 독립적인 전송 및 반사 계수 (TRC)에 대한 일반적인 가정에서 벗어납니다. 대신, 우리는 결합된 TRC 위상 변화 모델을 포함한 UAV 장착 STAR-RIS (Aerial-STAR)을 활용하는 혁신적인 다중 사용자 다운링크 통신 시스템을 탐구합니다. 우리의 주요 기여는 UAV 궤적, 기지국의 활성 빔포밍 벡터 및 수동 RIS TRC의 공동 최적화를 통해 통신 효율성을 향상시키는 동시에 UAV 에너지 제약을 고려합니다. 우리는 TRC를 이산 및 연속적인 조치의 조합으로 설계하고, 새로운 이중 액터 딥 결정적 정책 그래디언트 (DA-DDPG) 알고리즘을 제안합니다. 이 알고리즘은 고차원 하이브리드 액션 공간을 위해 두 개의 별도의 액터 네트워크에 의존합니다. 또한 사용자 간 통신 공정성을 보장하기 위해 새로운 조화평균 지수 (HFI) 기반 보상 함수를 제안합니다. 포괄적인 분석을 위해 RIS 크기가 UAV 공기역학에 미치는 영향을 연구하였으며, 이는 항력과 에너지 수요를 증가시킨다는 것을 보여줍니다. 시뮬레이션 결과는 제안된 DA-DDPG 알고리즘이 누적 보상에서 전통적인 DDPG 및 DQN 기반 솔루션을 각각 24% 및 97% 능가한다는 것을 보여줍니다. 3차원 UAV 궤적 최적화는 2차원 및 고도 최적화에 비해 통신 효율성이 28% 높습니다. HFI 기반 보상 함수는 다른 벤치마크에 비해 41% 낮은 QoS 거부율을 제공합니다. 이동식 Aerial-STAR 시스템은 고정 배치된 대조군에 비해 우수한 성능을 보이며, 결합된 위상 STAR-RIS는 이중 송신/반사 RIS 및 전통적인 RIS 설정을 능가합니다. 이러한 결과는 Aerial-STAR 시스템의 잠재력과 우리가 제안한 DA-DDPG 접근 방식이 그들의 성능을 최적화하는 데 효과적임을 강조합니다.

## 📝 요약

본 연구는 기존의 공기중 동시 송수신 재구성 지능 표면 (STAR-RIS) 연구에서 독립적인 송수신 계수(TRC)를 가정하는 것에서 벗어나, 복합 TRC 위상 변화 모델을 활용하는 UAV 장착 STAR-RIS(Aerial-STAR)을 이용한 새로운 다중 사용자 다운링크 통신 시스템을 탐구한다. 핵심 기여는 UAV 궤적, 기지국의 활성 빔포밍 벡터, 수동 RIS TRC의 공동 최적화를 통해 통신 효율성을 향상시키는 것이며, UAV 에너지 제약을 고려한다. TRC는 이산 및 연속적인 조치의 조합으로 설계되었고, 새로운 이중 액터 딥 결정적 정책 그래디언트(DA-DDPG) 알고리즘을 제안한다. 시뮬레이션 결과는 제안된 DA-DDPG 알고리즘이 누적 보상에서 기존 DDPG 및 DQN 기반 솔루션보다 24% 및 97% 우수함을 보여준다. 3차원 UAV 궤적 최적화는 2차원 및 고도 최적화에 비해 통신 효율성을 28% 향상시킨다. HFI 기반 보상 함수는 다른 벤치마크에 비해 41% 낮은 QoS 거부율을 제공한다. 모바일 Aerial-STAR 시스템은 고정 배치된 대조군보다 우수한 성능을 보이며, 결합 위상 STAR-RIS는 이중 송신/반사 RIS 및 기존 RIS 설정을 능가한다. 이러한 결과는 Aerial-STAR 시스템의 잠재력과 제안된 DA-DDPG 접근 방식의 성능 최적화 효과를 강조한다.

## 🎯 주요 포인트


- 1. UAV를 활용한 STAR-RIS 통신 시스템의 효율을 향상시키기 위한 다양한 최적화 방법을 제안하였다.

- 2. DA-DDPG 알고리즘을 통해 통신 효율을 24%와 97% 향상시켰으며, 통신 공정성을 보장하기 위한 HFI 기반 보상 함수를 제안하였다.

- 3. 3차원 UAV 궤적 최적화는 2차원 및 고도 최적화보다 28% 높은 통신 효율을 달성하였다.


---

*Generated on 2025-09-18 16:16:58*