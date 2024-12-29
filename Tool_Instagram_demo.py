import instaloader
import time
from colorama import Fore, Style, init

# Khởi tạo colorama để hỗ trợ màu
init(autoreset=True)

# Logo ASCII
logo = """
🟦🟦🟦🟦🟦🟦🟪🟪🟪🟪🟪🟪🟪🟪🟪
🟦🟦🟦🟦🟦🟦🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
🟦🟦🟦🟦🟦🟦🟦🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
🟪🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟪🟪🟪🟪
🟪🟪🟪⬜🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜🟪🟪🟪
🟪🟪🟪⬜🟪🟪🟪🟪🟪🟪🟪🟪⬜⬜🟪⬜🟪🟪🟪
🟪🟪🟪⬜🟪🟪🟪🟪🟪🟪🟪🟪⬜⬜🟪⬜🟪🟪🟪
🟪🟪🟪⬜🟪🟪🟪⬜⬜⬜⬜🟪🟪🟪🟪⬜🟪🟪🟪
🟪🟪🟪⬜🟥🟪⬜🟪🟪🟪🟪⬜🟪🟪🟪⬜🟪🟪🟪
🟪🟪🟥⬜🟥🟥⬜🟪🟥🟪🟪⬜🟪🟪🟪⬜🟪🟪🟪
🟥🟥🟥⬜🟥🟥⬜🟥🟥🟥🟥⬜🟪🟪🟪⬜🟪🟪🟪
🟥🟥🟧⬜🟧🟧⬜🟧🟧🟥🟥⬜🟥🟪🟪⬜🟪🟪🟪
🟧🟧🟧⬜🟨🟧🟧⬜⬜⬜⬜🟥🟥🟥🟥⬜🟪🟪🟪
🟧🟨🟨⬜🟨🟨🟧🟧🟧🟧🟥🟥🟥🟥🟥⬜🟪🟪🟪
🟧🟨🟨⬜🟨🟨🟧🟧🟧🟧🟥🟥🟥🟥🟥⬜🟪🟪🟪
🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟪🟪🟥🟥
🟨🟨🟨🟨🟨🟨🟨🟨🟧🟧🟧🟧🟧🟥🟥🟥🟥🟥🟥
🟨🟨🟨🟨🟨🟨🟨🟨🟧🟧🟧🟧🟥🟥🟥🟥🟥
🟨🟨🟨🟨🟨🟨🟨🟧🟧🟧🟧🟥🟥🟥🟥
"""

# Danh sách các khóa hợp lệ
keys = ['userKey202422', 'userKey202423', 'userKey202424']  # Thêm các khóa hợp lệ vào đây

# Kiểm tra khóa người dùng nhập
key = input(Fore.GREEN + "Nhập khóa truy cập: ").strip()
print(Fore.CYAN + "\nNhập khóa thành công!")

if key not in keys:
    print(Fore.RED + "\n[!] Khóa không hợp lệ! Vui lòng mua khóa.")
    print("Discord: Ssleck | Zalo: 0866683053\n")
else:
    while True:
        # Hiển thị menu lựa chọn
        print(Fore.YELLOW + "\nChọn một tùy chọn:")
        print("1. Vào tool Instagram")
        print("2. Vào tính năng khác (đang phát triển)")
        print("0. Thoát chương trình")

        try:
            choice = input(Fore.CYAN + "\nNhập lựa chọn của bạn: ").strip()

            if choice == '1':
                # Tool Instagram
                loader = instaloader.Instaloader()

                # Hiển thị logo
                print(Fore.YELLOW + logo)

                # Sử dụng session đã lưu nếu có
                try:
                    loader.load_session_from_file('your_session_name')  # Tải session từ file
                    print(Fore.GREEN + "Đã sử dụng phiên đăng nhập hiện tại.")
                except FileNotFoundError:
                    print(Fore.RED + "Không tìm thấy phiên làm việc. Đang tạo phiên mới...")
                    try:
                        # Đăng nhập lại nếu session không hợp lệ
                        username_instagram = input(Fore.GREEN + "\nNhập tên tài khoản Instagram của bạn: ").strip()
                        password_instagram = input(Fore.GREEN + "Nhập mật khẩu tài khoản Instagram của bạn: ").strip()

                        loader.login(username_instagram, password_instagram)  # Đăng nhập vào Instagram
                        loader.save_session_to_file('your_session_name')  # Lưu session vào file
                        print(Fore.GREEN + f"\nĐăng nhập thành công với tài khoản {username_instagram}!")
                    except instaloader.exceptions.BadCredentialsException:
                        print(Fore.RED + "\n[Lỗi] Sai tên người dùng hoặc mật khẩu.")
                        continue

                while True:
                    try:
                        # Nhập tên Instagram của người cần kiểm tra
                        username = input(Fore.BLUE + "\nNhập tên người dùng Instagram: ")

                        # Lấy thông tin của profile
                        profile = instaloader.Profile.from_username(loader.context, username)
                        initial_post_count = profile.mediacount  # Lưu số lượng bài viết ban đầu

                        print(f"\nSố lượng bài viết ban đầu của {username}: {initial_post_count}")

                        # Hiển thị thông tin người dùng
                        print(Fore.GREEN + "\nThông tin người dùng Instagram:")
                        print(f" - Tên đầy đủ: {profile.full_name}")
                        print(f" - ID: {profile.userid}")
                        print(f" - Số lượng bài viết: {profile.mediacount}")
                        print(f" - Số lượng người theo dõi: {profile.followers}")
                        print(f" - Số lượng đang theo dõi: {profile.followees}")
                        print(f" - Có phải tài khoản riêng tư không? {'Có' if profile.is_private else 'Không'}")
                        print(f" - Có phải tài khoản đã xác minh không? {'Có' if profile.is_verified else 'Không'}")

                        # Liên kết đến trang Instagram
                        profile_link = f"https://www.instagram.com/{username}/"
                        print(f"Liên kết đến trang cá nhân Instagram: {profile_link}")

                        # Liên kết trang cá nhân facebook
                        try:
                            fb_link = profile.get_profile_pic_url()
                            if fb_link:
                                print(f"Liên kết Facebook: {fb_link}")
                        except:
                            print("Không có liên kết Facebook.")

                        # Tải ảnh nếu chọn 'y'
                        download_choice = input(Fore.YELLOW + "\nBạn có muốn tải ảnh bài viết không? (y/n): ").strip().lower()

                        if download_choice == 'y':
                            resolution_choice = input("Bạn có muốn tải ảnh với độ phân giải cao không? (y/n): ").strip().lower()

                            if resolution_choice == 'y':
                                print(Fore.CYAN + "\nĐang tải ảnh với độ phân giải cao...")
                                for post in profile.get_posts():
                                    loader.download_post(post, target=username)
                            else:
                                print(Fore.CYAN + "\nBắt đầu tải ảnh bài viết...")
                                for post in profile.get_posts():
                                    loader.download_post(post, target=username)
                            
                            print(Fore.GREEN + f"\nHoàn thành tải xuống ảnh bài viết của {username}!")

                            # Kiểm tra có muốn xem thông tin chi tiết bài viết không
                        check_posts = input("\nBạn có muốn kiểm tra thông tin chi tiết các bài viết không? (y/n): ").strip().lower()
                        if check_posts == 'y':
                            print("\nThông tin chi tiết các bài viết:")
                            for post in profile.get_posts():
                                print(f"\n--- Bài viết ---")
                                print(f" - Caption: {post.caption}")
                                print(f" - Lượt thích: {post.likes}")
                                print(f" - Số bình luận: {post.comments}")
                                print(f" - Ngày đăng: {post.date_utc}")
                                print(f" - Liên kết bài viết: https://www.instagram.com/p/{post.shortcode}/")

                        # Bắt đầu theo dõi số lượng bài viết
                        follow_choice = input("\nBạn có muốn theo dõi số lượng bài viết không? (y/n): ").strip().lower()

                        if follow_choice == 'y':
                            while True:
                                profile = instaloader.Profile.from_username(loader.context, username)
                                current_post_count = profile.mediacount

                                if current_post_count != initial_post_count:
                                    print(f"\n[Cập nhật] Số lượng bài viết đã thay đổi từ {initial_post_count} lên {current_post_count}.")
                                    initial_post_count = current_post_count

                                time.sleep(30)  # Lặp lại mỗi 30 giây
                        else:
                            print("\nDừng theo dõi số lượng bài viết.")

                    except instaloader.exceptions.ProfileNotExistsException:
                        print(Fore.RED + "\n[Lỗi] Tên người dùng không tồn tại.")
                    except instaloader.exceptions.ConnectionException:
                        print(Fore.RED + "\n[Lỗi] Không thể kết nối tới Instagram.")
                    except Exception as e:
                        print(Fore.RED + f"\n[Lỗi không xác định] {e}")

                    # Sau khi hoàn thành một tài khoản, tiếp tục với tài khoản khác hoặc quay lại menu chính
                    continue_choice = input(Fore.YELLOW + "\nBạn có muốn kiểm tra tài khoản khác không? (y/n): ").strip().lower()
                    if continue_choice != 'y':
                        break

            elif choice == '2':
                # Placeholder cho tính năng khác
                print(Fore.CYAN + "\nTính năng này đang được phát triển. Vui lòng thử lại sau.")

            elif choice == '0':
                print(Fore.GREEN + "\nCảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
                break

            else:
                print(Fore.RED + "\n[Lỗi] Lựa chọn không hợp lệ. Vui lòng chọn lại.")

        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Chương trình đã dừng.")
            break