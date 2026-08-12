import streamlit as st
from database import init_db

init_db()

st.set_page_config(
    page_title="Project Manager",
    page_icon="✳️",
    layout="wide"
)

st.title("⏲️ Project Manager")

st.markdown("""
*Chào mừng đến với phần mềm quản lý dự án cá nhân của* `├───┤oang💫Tri`

---

# Cảm ngộ

## Sự đột phá
- Giống như nhốt mình trong một căn phòng tối om, bên trong phòng chỉ có một cửa sổ sáng mịt mờ. Gục trước cửa sổ tựa hồ có thể mông lung cảm nhận được thế giới bên ngoài, phảng phất có núi, có cây, có người, còn có hoa thơm bướm lượn, thậm chí có tiếng nước chảy rào rào, làm cho ngươi vô cùng nôn nóng _muốn ra ngoài, nhìn thế giới_ rút cuộc như thế nào. 
- Nhưng hắn lại không cách nào đâm phá được chiếc cửa sổ kia, tựa như cửa sổ được làm bằng da trâu gân hồ siêu dai, bất luận ngươi dùng hết biện pháp gì cũng không thể đâm được. Có đôi khi cảm giác phảng phất đã đạt đến đột phá, phảng phất có thể dễ dàng đâm thủng chiếc cửa sổ kia, nhưng cuối cùng lại vỡ mộng, làm cho người ta phát điên, tinh thần uể oải. 
- Đây là sự _lột xác_ từ con sâu lông thành con bướm. Trải quá từng bước bò trườn chậm chạp, kinh qua sự từng trải và tích lũy dài lâu, sau đó yên tĩnh trở lại lắng đọng nội liễm kết thành cái kén, lẳng lặng chờ đợi ngày phá kén trùng sinh.

## Thái độ
- Trong cuộc sống, những chuyện ta không mong muốn vẫn luôn xảy ra. Chẳng hạn, nhỏ thì như chuyện: cơm sống, canh mặn; hoặc lớn hơn như chuyện: trẻ con hàng xóm đánh nhau hay anh chồng nhậu say xỉn… _Bản thân chúng chưa phải là vấn đề; chính thái độ và cách xử lý không thích hợp của chúng ta mới thực sự biến chúng thành vấn đề._

## Sự rèn luyện
- Dù kĩ thuật gì đẹp đẽ đến đâu nếu bóc đi lớp vỏ hào nhoáng bên ngoài, bên trong nhất định là do hơn hàng trăm ngàn loại _đơn điệu, buồn tẻ, rèn luyện một cách máy móc_ mà thành. Mỗi một bậc tăng lên thường phải kiên trì không ngừng rèn luyện trên ngàn vạn lần.

## Âm mưu
- Hùng tại đại lược, có người sinh ra đã có, nhưng tuyệt đại bộ phận là do rèn luyện được, người nắm quyền lực trong tay, thì chỉ cần bảy phần thắng là sẽ làm ngay, không có chút do dự nào, trên đời làm gì có chuyện gì nắm chắc thắng lợi mười phần. Nếu như có một ngày, bản thân ngươi có loại cảm giác này thì phải _đề cao cảnh giác, vì nguy hiểm đã đến rất gần_, vì nếu như người nắm chắc cả mười phần thì chứng tỏ rất có khả năng là kẻ địch cho ngươi tin tức sai lầm, để ngươi buông lỏng, hắn sẽ tấn công vào chỗ ngươi không ngờ tới.

## Nhân sinh
- Điều thú vị của đời người chính là ở đây, _tương lai là thứ không có cách nào mò bắt được_, bọn ta chỉ đành tùy cơ ứng biến, cố gắng hết sức mình.
""")
