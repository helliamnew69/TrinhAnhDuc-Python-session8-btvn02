shop_name = ""
product_name = ""
product_description = ""
product_category = ""
keyword_list = []
discount_codes = []

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM =====")
    print("1. Nhập dữ liệu sản phẩm")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    match choice:

        case "1":

            shop_name = input("Nhập tên shop: ").strip()

            if shop_name == "":
                print("Tên shop không được bỏ trống")
                continue

            product_name = input("Nhập tên sản phẩm: ").strip()

            product_description = input("Nhập mô tả sản phẩm: ").strip()

            if product_description == "":
                print("Mô tả sản phẩm không được rỗng")
                continue

            product_category = input("Nhập danh mục: ").strip().lower()

            keywords = input("Nhập danh sách từ khóa: ")

            keyword_list = keywords.split(",")

            clean_keywords = []

            for keyword in keyword_list:
                clean_keywords.append(keyword.strip())

            keyword_list = clean_keywords

            print("\n===== BÁO CÁO =====")

            print("Tên shop:", shop_name)
            print("Tên sản phẩm:", product_name.title())
            print("Mô tả:", product_description)

            print("Độ dài mô tả:", len(product_description))

            print("Danh mục:", product_category)

            print("Danh sách từ khóa:", keyword_list)

            print("Số lượng từ khóa:", len(keyword_list))

            print("Mô tả chữ thường:")
            print(product_description.lower())

            print("Mô tả chữ hoa:")
            print(product_description.upper())

        case "2":

            raw_shop = input("Nhập tên shop: ")

            if raw_shop.strip() == "":
                print("Tên shop không được bỏ trống")

            else:

                new_shop = raw_shop.strip().lower()
                new_shop = new_shop.replace(" ", "-")

                if not new_shop.startswith("shop-"):
                    new_shop = "shop-" + new_shop

                print("Tên ban đầu:", raw_shop)
                print("Tên chuẩn hóa:", new_shop)

        case "3":

            code = input("Nhập mã giảm giá: ")

            if code == "":
                print("Mã giảm giá không được rỗng")

            elif " " in code:
                print("Mã giảm giá không được chứa khoảng trắng")

            elif len(code) < 6 or len(code) > 12:
                print("Mã giảm giá phải dài từ 6 đến 12 ký tự")

            elif code != code.upper():
                print("Mã giảm giá phải viết hoa toàn bộ")

            elif not code.isalnum():
                print("Mã chỉ được chứa chữ và số")

            elif not code.startswith("SALE"):
                print("Mã phải bắt đầu bằng SALE")

            else:
                print("Mã giảm giá hợp lệ")

                discount_codes.append(code)

                print("Danh sách mã hiện tại:")
                print(discount_codes)

        case "4":

            if product_description == "":
                print("Chưa có mô tả sản phẩm")
                continue

            old_word = input("Nhập từ khóa cần tìm: ")
            new_word = input("Nhập từ khóa thay thế: ")

            if old_word in product_description:

                count = product_description.count(old_word)

                new_description = product_description.replace(
                    old_word,
                    new_word
                )

                print("Số lần xuất hiện:", count)

                print("Mô tả sau khi thay thế:")
                print(new_description)

            else:
                print("Không tìm thấy từ khóa")

        case "5":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")