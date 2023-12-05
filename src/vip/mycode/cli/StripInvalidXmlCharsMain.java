package vip.mycode.cli;

import vip.mycode.stringutils.StripInvalidChars;
import vip.mycode.stringutils.StripInvalidXmlChars;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * @author shiqi
 * @date 2023/12/05 22:04
 */
public class StripInvalidXmlCharsMain
{
    /**
     * 从Reader中读取每一行数据，使用StripInvalidChars对象对每一行进行处理，然后将处理后的数据写入Printer中。
     *
     * @param reader 用于读取数据的BufferedReader对象
     * @param writer 用于写入数据的PrintWriter对象
     * @param stripHandler 用于处理数据的StripInvalidChars对象
     * @return 如果成功处理数据并写入，则返回true；否则返回false
     */
    public static boolean doStrip(BufferedReader reader,
                               PrintWriter writer,
                               StripInvalidChars stripHandler)
    {
        if (reader == null
                || writer == null
                || stripHandler == null) {
            return false;
        }
        
        try {
            String line;
            while ((line = reader.readLine()) != null) {
                writer.println(stripHandler.stripInvalidChars(line));
            }
            
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        return false;
    }

    
    /**
     * 主函数
     *
     * @param args 命令行参数
     * @throws IOException 输入输出异常
     */
    public static void main(String[] args) throws IOException {
        int argc = args.length;
        if (argc < 1 || argc > 2) {
            System.err.println("usage: INPUT_XML_PATH [OUTPUT_XML_PATH]");
            System.exit(-1);
        }

        String inputFilePath = args[0];
        String outputFilePath = null;
        if (argc == 2) {
            outputFilePath = args[1];
        }

        BufferedReader reader = null;
        PrintWriter writer = null;

        try {
            reader = new BufferedReader(new FileReader(inputFilePath));
            if (outputFilePath != null) {
                writer = new PrintWriter(new FileWriter(outputFilePath));
            } else {
                writer = new PrintWriter(System.out);
            }

            boolean ret = doStrip(reader, writer, new StripInvalidXmlChars());
            if (!ret) {
                System.err.println("Failed to strip invalid XML chars.");
                System.exit(-1);
            }

            System.out.println("Done.");
            System.exit(0);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                reader.close();
            }
            if (writer != null) {
                writer.close();
            }
        }
    }

}


 