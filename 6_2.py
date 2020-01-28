sp = float(input("Enter the selling price of item : "))
gst_rate = float(input("Enter the gst rate : "))
sgst_rate = gst_rate/2
gst = sp * 0.01 * gst_rate
sgst = cgst = sp * 0.01 * sgst_rate
total = sp+gst
print("Selling Price            :", sp)
print("GST@" + str(gst_rate)+ "% :" )
print("CSGT                     :" , cgst)
print("SGST                     :" , sgst)
print("                         :" , gst)
print("Total                    :" , total)

