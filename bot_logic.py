"python.analysis.diagnosticSeverityOverrides" :{
        "reportMissingImports" : "none"}python
import datetime
import hashlib
import random
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

# تعريفات الفئات والأنواع (ReportStatus, SupportType, CorruptionReport, User, Asset, Transaction)
# و ElectronicMindSystem
# يجب أن تكون هذه التعريفات موجودة في نفس الملف أو ملف آخر يتم استيراده.
# لتبسيط الأمر، سأفترض أنها موجودة في نفس الملف مؤقتاً.
# (في بيئة Codespaces، يمكنك وضعها في نفس الملف أو في ملف منفصل واستيرادها)

# --- بداية الكود الكامل لنظام العقل الإلكتروني (للتوضيح فقط، لا تلصق هذا الجزء مرتين) ---
# (هذا الجزء يجب أن يكون موجوداً بالفعل في ملفك)
class ReportStatus(Enum):
    PENDING = "قيد المراجعة"
        REVIEWED = "تمت المراجعة"
            INVESTIGATING = "قيد التحقيق"
                RESOLVED = "تم الحل"

                class SupportType(Enum):                  BREAD = "دعم خبز"
                        FOOD = "دعم غذائي"
                            CASH = "دعم نقدي"
                                NONE = "غير مؤهل                               @dataclass
                            class CorruptionReport:
                                    id: str
                                        user_id: str
                                            description: str
                                                location: str
                                                    timestamp: datetime.datetime
                                                        status: ReportStatus
                                                            risk_score: float
                                                                keywords: List[str]

                                                                @dataclass
                                                                class User:
                                                                    national_id: str
                                                                        name: str
                                                                            income: float
                                                                                family_members: int
                                                                                    has_property: bool
                                                                                        phone: str

                                                                                        @dataclass
                                                                                        class Asset:
                                                                                            id: str
                                                                                                owner_id: str
                                                                                                    asset_type: str
                                                                                                        value: float
                                                                                                            description: str
                                                                                                                registration_date: datetime.datetime

                                                                                                                @dataclass
                                                                                                                class Transaction:
                                                                                                                    id: str
                                                                                                                        from_user: str
                                                                                                                            to_user: str
                                                                                                                                amount: float
                                                                                                                                    transaction_type: str
                                                                                                                                        timestamp: datetime.datetime
                                                                                                                                            description: str

                                                                                                                                            class ElectronicMindSystem:
                                                                                                                                                def __init__(self):
                                                                                                                                                        self.reports: List[CorruptionReport] = []
                                                                                                                                                                self.users: Dict[str, User] = {}
                                                                                                                                                                        self.assets: Dict[str, List[Asset]] = {}
                                                                                                                                                                                self.transactions: Dict[str, List[Transaction]] = {}
                                                                                                                                                                                        self.resources_data: Dict[str, List[Dict]] = {}
                                                                                                                                                                                                
                                                                                                                                                                                                        self._initialize_sample_data()
                                                                                                                                                                                                            
                                                                                                                                                                                                                def _initialize_sample_data(self):
                                                                                                                                                                                                                        sample_users = [
                                                                                                                                                                                                                                    User("12345678901234", "أحمد محمد", 3500, 4, False, "01234567890"),
                                                                                                                                                                                                                                                User("23456789012345", "فاطمة علي", 2800, 3, False, "01123456789"),
                                                                                                                                                                                                                                                            User("34567890123456", "محمد حسن", 6000, 2, True, "01012345678")
                                                                                                                                                                                                                                                                    ]
                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                    for user in sample_users:
                                                                                                                                                                                                                                                                                                self.users[user.national_id] = user
                                                                                                                                                                                                                                                                                                            self.assets[user.national_id] = []
                                                                                                                                                                                                                                                                                                                        self.transactions[user.national_id] = []
                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                        sample_assets = [
                                                                                                                                                                                                                                                                                                                                                    Asset("asset_001", "34567890123456", "عقار", 1500000, "شقة 120 متر", datetime.datetime.now()),
                                                                                                                                                                                                                                                                                                                                                                Asset("asset_002", "34567890123456", "سيارة", 300000, "تويوتا كامري 2020", datetime.datetime.now())
                                                                                                                                                                                                                                                                                                                                                                        ]
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                        for asset in sample_assets:
                                                                                                                                                                                                                                                                                                                                                                                                    self.assets[asset.owner_id].append(asset)
                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                    sample_transactions = [
                                                                                                                                                                                                                                                                                                                                                                                                                                Transaction("tx_001", "12345678901234", "shop_001", 150, "شراء", 
                                                                                                                                                                                                                                                                                                                                                                                                                                                       datetime.datetime.now(), "شراء مواد غذائية"),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Transaction("tx_002", "23456789012345", "12345678901234", 500, "تحويل",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          datetime.datetime.now() - datetime.timedelta(days=2), "تحويل مساعدة")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  for tx in sample_transactions:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              if tx.from_user not in self.transactions:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              self.transactions[tx.from_user] = []
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          self.transactions[tx.from_user].append(tx)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          self.resources_data["دقيق"] = [
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"quantity": 1000, "date": "2025-09-18", "location": "مطحن القاهرة"},
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"quantity": 800, "date": "2025-09-19", "location": "مطحن الجيزة"},