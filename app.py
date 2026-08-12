import streamlit as st
from database import init_db

init_db()

st.set_page_config(
    page_title="my-Project",
    page_icon="✔️",
    layout="wide"
)

st.title("✅ Project Manager")

st.markdown("""
*Chào mừng đến với phần mềm quản lý dự án cá nhân của* `├───┤oang💫Tri`

---

# Cảm ngộ tự thân

## Đột phá
- Cảm giác giống như nhốt mình trong một căn phòng tối om, bên trong phòng chỉ có một cửa sổ sáng mịt mờ. Gục trước cửa sổ tựa hồ có thể mông lung cảm nhận được thế giới bên ngoài, phảng phất có núi, có cây, có người, còn có hoa thơm bướm lượn, thậm chí có tiếng nước chảy rào rào, làm cho ngươi vô cùng nôn nóng _muốn ra ngoài, nhìn thế giới_ rút cuộc như thế nào. 
- Nhưng ta lại không cách nào đâm phá được chiếc cửa sổ kia, tựa như cửa sổ được làm bằng da trâu gân hồ siêu dai, bất luận dùng biện pháp gì cũng không thể đâm được. Có đôi khi cảm giác phảng phất đã đạt đến đột phá, phảng phất có thể dễ dàng đâm thủng chiếc cửa sổ kia, nhưng cuối cùng lại vỡ mộng, làm cho người ta phát điên, tinh thần uể oải. 
- Đây là sự **lột xác** từ con sâu lông thành con bướm. Trải quá từng bước bò trườn chậm chạp, kinh qua sự từng trải và tích lũy dài lâu, sau đó yên tĩnh trở lại lắng đọng nội liễm kết thành cái kén, lẳng lặng chờ đợi ngày phá kén trùng sinh.
- Cảm giác, cuối cùng là một loại năng lực của con người, một loại tiềm năng. Vô luận năng lực gì, càng gặp hoàn cảnh tàn khốc, càng dễ dàng phát triển rất nhanh.
- Trong nháy mắt hắn tựa hồ cảm nhận được sự huyền bí vận hành trong vũ trụ mênh mông, biết được tại sao nam nhân không thể rời bỏ nữ nhân, nữ nhân tại sao không thể rời bỏ nam nhân, bởi vì cần một điểm thăng bằng, chỉ có đạt đến điểm thăng bằng nào đó mới có thể sống vĩnh hằng.
- Trong lòng không sợ, cảnh giới là vô bờ. 

## Mưu lược
- Phép dụng binh, là lấy mưu làm chính! 
    - Đó là dùng mưu lược trận, trước tiên phải mưu đoạt địa lợi; muốn dùng mưu thắng địch, trước tiên phải dùng mưu đặt bản thân vào thế bất bại.
- Dũng cảm hay nhát gan là tại phương pháp, thành hay bại là tại trí. 
    - Nghĩa là dũng cảm hay nhát gan nằm ở mưu, mạnh hay yếu nằm ở thế. 
        - Mưu đạt, việc thành thì làm người dũng. 
        - Mưu hỏng, thế mất thì làm người nhát gan giả dũng cảm.
- Nước có nội loạn, không thể xuất binh; lòng quân không yên không thể ra trận; trận thế không chắc chắn, thì không thể đánh; không đồng lòng đánh, tất không thể quyết chiến.

## Sinh mệnh
- Không có sinh, không có tử. Sinh mệnh chỉ là một trò chơi nhỏ đang ngẫu nhiên diễn ra trong vũ trụ.
    - Giống như đức tính, phẩm hạnh khi còn trẻ, quyết định điều kiện sinh sống lúc tuổi già; đời sống cõi trần quyết định đời sống bên kia cửa tử.
- Thiên đạo tuần hoàn, dương cực âm sinh, âm tiêu dương phục, tận sinh là tử, tận tử là sinh, đó là đạo lý của Trời Đất.
- Đây là con đường chính ngươi chọn, đau khổ, vui vẻ dọc trên đường đi phải do bản thân ngươi gánh vác.
- Nước có nạn tất sinh anh hùng, trời sắp sập tất có yêu nghiệt. Khi thiên địa gặp nguy, chắc chắn sẽ có những người gánh vác khí vận thiên địa mà sinh ra.
- Chỉ cần là con người thì chắc chắn sẽ có những khúc mắc trong lòng, đó chính là bản chất.
- Sống trọng yếu hơn bất cứ cái gì, sống sót chính là may mắn lớn nhất.
- Nếu không dám khiêu chiến với giới hạn sinh tử, thì làm sao có thể ngộ được đạo một cách thực sự, có thể nắm được lực lượng một cách chân chính?
- Thay vì tìm một chân lý tuyệt đối, hãy tìm sự tuyệt đối nơi mình vì chân lý để sống chứ không phải để dạy.
- Mọi vật trong vũ trụ đều quân bình tuyệt đối, không dư, không thiếu, từ hạt bụi bé nhỏ đến những dãy thiên hà vĩ đại.
- Nếu có chết chỉ là hình hài, xác thân, chứ không phải sự sống, và hình hài có chết đi, thì sự sống mới tiếp tục tiến hóa ở một thể khác, tinh vi hơn.

## Thái độ
- Trong cuộc sống, những chuyện ta không mong muốn vẫn luôn xảy ra. 
    - Chẳng hạn, nhỏ thì như chuyện: cơm sống, canh mặn; hoặc 
    - Lớn hơn như chuyện: trẻ con hàng xóm đánh nhau hay anh chồng nhậu say xỉn… 
    > **Bản thân chúng chưa phải là vấn đề; chính thái độ và cách xử lý không thích hợp của chúng ta mới thực sự biến chúng thành vấn đề.**
- Sáng tạo bất chiếm hữu, Thành công bất tự cứ. 
- Tìm kiếm quy luật từ trong thất bại.
- Không ngừng mô phỏng các loại tình huống để lựa chọn kỹ năng cần thiết.
- Không nên buông tha hy vọng khi đang mệt mỏi, lực lượng đến từ chính khát vọng.
- Lúc bình thường mới lộ ra bản tính.
- Sự thật là không có điều gì chia cách linh hồn cả, khi ta yêu mến ai bằng những rung động chân thành, ta yêu mến họ qua linh hồn của họ chứ đâu phải chỉ qua xác thân.

## Rèn luyện
- Dù kĩ thuật gì đẹp đẽ đến đâu nếu bóc đi lớp vỏ hào nhoáng bên ngoài, bên trong nhất định là do hơn hàng trăm ngàn loại _đơn điệu, buồn tẻ, rèn luyện một cách máy móc_ mà thành. Mỗi một bậc tăng lên thường phải kiên trì không ngừng rèn luyện trên ngàn vạn lần.
- Cảm giác được mọi người thừa nhận là rất thần kì, chỉ khi có cảm giác thì mới có thể giao tiếp với năng lượng, mà những người có cảm giác mạnh mẽ thì thậm chí có thể khống chế hình dạng và kết cấu của năng lượng
- Hình thái càng cơ bản thì càng dễ tìm hiểu đến bản chất của sự vật, đây là quy luật.
- Chi cần ngươi nghĩ ra là đều có thể làm được, chỉ là khác biệt về hình thái mà thôi. Dĩ nhiên chuyện này được quyết định bởi khả năng khống chế của ngươi.
- Không ai tận tình dạy bảo điều gì, tất cả đều dựa vào sự lĩnh ngộ của bản thân, dùng thương tích và cơ thể của mỉnh để cảm nhận. Cái gì được dạy dỗ, chung quy là của người khác, lĩnh ngộ mới là của chính mình.
""")
