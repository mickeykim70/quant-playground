import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView

# 기존 콘솔 버전에서 만들었던 Contact 클래스를 그대로 사용하거나, GUI용으로 정의합니다.
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 윈도우 타이틀 및 크기 설정
        self.setWindowTitle("주소록 GUI - Phase 3")
        self.setGeometry(100, 100, 400, 300)

        # 메인 레이아웃 설정 (세로 방향)
        layout = QVBoxLayout()

        # 이름 입력 영역
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(QLabel("이름:"))
        self.name_input = QLineEdit()
        h_layout1.addWidget(self.name_input)
        layout.addLayout(h_layout1)

        # 전화번호 입력 영역
        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(QLabel("전화번호:"))
        self.phone_input = QLineEdit()
        h_layout2.addWidget(self.phone_input)
        layout.addLayout(h_layout2)

        # 이메일 입력 영역
        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(QLabel("이메일:"))
        self.email_input = QLineEdit()
        h_layout3.addWidget(self.email_input)
        layout.addLayout(h_layout3)

        # 주소 입력 영역
        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(QLabel("주소:"))
        self.address_input = QLineEdit()
        h_layout4.addWidget(self.address_input)
        layout.addLayout(h_layout4)

        # 저장 버튼 생성 및 클릭 이벤트 연결
        self.save_btn = QPushButton("저장")
        self.save_btn.clicked.connect(self.save_contact)
        layout.addWidget(self.save_btn)

        # 연락처 목록 표(Table) 추가
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["이름", "전화번호", "이메일", "주소"])
        # 표의 너비를 자동으로 조절
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        # 중앙 위젯을 생성하여 레이아웃 적용
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 시작할 때 기존 데이터 불러오기
        self.load_contacts_to_table()

    def load_contacts_to_table(self):
        """파일에서 데이터를 읽어와 표(Table)에 표시하는 함수"""
        if not os.path.exists("contact_db.txt"):
            return

        # 표 내용 초기화
        self.table.setRowCount(0)

        try:
            with open("contact_db.txt", "rt", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip():
                        # 데이터를 / 구분자로 나누기
                        data = line.strip().split("/")
                        if len(data) == 4:
                            # 표에 새로운 행 추가
                            row_count = self.table.rowCount()
                            self.table.insertRow(row_count)
                            # 각 칸에 데이터 채우기
                            for col, item in enumerate(data):
                                self.table.setItem(row_count, col, QTableWidgetItem(item))
        except Exception as e:
            QMessageBox.critical(self, "오류", f"데이터를 불러오는 중 오류가 발생했습니다: {e}")

    def save_contact(self):
        """입력 필드의 데이터를 읽어와서 파일에 저장하는 함수"""
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        # 입력값이 비어있는지 간단히 체크
        if name == "" or phone == "":
            QMessageBox.warning(self, "경고", "이름과 전화번호는 필수 입력 항목입니다.")
            return

        # 파일에 저장 (추가 모드로 열기)
        try:
            with open("contact_db.txt", "at", encoding="utf-8") as f:
                f.write(f"{name}/{phone}/{email}/{address}\n")
            
            QMessageBox.information(self, "완료", f"{name} 님의 연락처가 저장되었습니다.")
            
            # 저장 후 입력창 초기화
            self.name_input.clear()
            self.phone_input.clear()
            self.email_input.clear()
            self.address_input.clear()

            # 표(Table) 새로고침
            self.load_contacts_to_table()
            
        except Exception as e:
            QMessageBox.critical(self, "오류", f"저장 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    # 애플리케이션 실행 루프 시작
    app = QApplication(sys.argv)
    window = ContactGUI()
    window.show()
    sys.exit(app.exec_())
