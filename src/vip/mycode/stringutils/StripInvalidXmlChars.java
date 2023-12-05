package vip.mycode.stringutils;

/**
 *
 * @author shiqi
 * @date 2023/12/1 00:49
 * @description TODO
 */
public class StripInvalidXmlChars implements StripInvalidChars
{
    /**
     * 判断指定字符是否为XML文件的非法字符
     *
     * @param c 要判断的字符
     * @return 如果字符为无效字符，则返回true；否则返回false
     */
    @Override
    public boolean isInvalidChar(char c)
    {
        return !isValidChar(c);
    }
    
    /**
     * 判断指定字符是否为XML文件的合法字符
     *
     * @param c 要判断的字符
     * @return 如果字符合法，则返回true；否则返回false
     */
    @Override
    public boolean isValidChar(char c)
    {
        // 如果字符是制表符、换行符、回车符，或者是Unicode字符范围内的字符，
        // 则属于Xml文件中的合法字符；除此以外属于无效字符。
        return ((c == 0x9)
                || (c == 0xA)
                || (c == 0xD)
                || ((c >= 0x20) && (c <= 0xD7FF))
                || ((c >= 0xE000) && (c <= 0xFFFD))
                || ((c >= 0x10000) && (c <= 0x10FFFF)));
    }
    
    /**
     * 重写的方法，用于去除无效字符
     *
     * @param input 输入的字符串
     * @return 去除无效字符后的字符串，如果input为null，则返回""
     */
    @Override
    public String stripInvalidChars(String input)
    {
        if (input == null || input.length() == 0) {
            return "";
        }
        
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            // 如果是非法的，跳过
            if (isInvalidChar(c)) {
                continue;
            }
            
            output.append(c);
        }
        
        return output.toString();
    }
    
}


 