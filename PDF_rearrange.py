from pypdf import PdfWriter

def takeInput() -> list:
    print("Do you want to specify page numbers [P] or interleaved [I](evens then odds)?")
    u_input = input()
    while u_input != "P" and u_input != "I":
        print("Unrecognised input. Please input \'P\' or \'I\', no quotations and capitalised")
        u_input = input()


    if u_input == 'P':
        print("Please provide the new order of the pages")
        print("E.g. \"3, 5, 7, 2, 4, 6\", this means 1st page omitted and then 3rd->5th->7th->2nd->4th->6th. No quotation marks required")
        try:
            page_array = input().split(',')
            page_array = [int(i) - 1 for i in page_array]
        except Exception as e:
            print(f"Unexpected error: {e}")
    else:
        print("Please provide the total number of pages")
        num = int(input())
        j = 0
        i = 0
        page_array = [0 for i in range(num)]
        while i <= num - 1:
            page_array[i] = j
            i += 2
            j += 1
        i = 1
        while i <= num - 1:
            page_array[i] = j
            i += 2
            j += 1
            
    return page_array

merger = PdfWriter()

def sliceMerge(order: list):
    print("Please provide the file name, including the extension")
    print("E.g. abc.pdf")
    file_name = input()
    file = open(file_name, "rb")
    
    for number in order:
        merger.append(fileobj = file, pages = (number, number + 1))

    output = open("reordered_output.pdf", "wb")
    merger.write(output)

    merger.close()
    output.close()
                
def main():
    listing = takeInput()
    sliceMerge(listing)

main()