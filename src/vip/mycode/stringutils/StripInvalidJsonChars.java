package vip.mycode.stringutils;

/**
 * @author shiqi
 * @date 2023/12/1 19:24
 * @description TODO
 */
public class StripInvalidJsonChars implements StripInvalidChars
{
    
    /**
     * 判断一个字符是否是非法的，如果非法字符则返回true，否则返回false
     *
     * @param ch 需要判断的字符
     * @return BOOLEAN true: 非法字符 false: 合法字符
     */
    @Override
    public boolean isInvalidChar(char ch)
    {
        return false;
    }
    
    /**
     * 判断一个字符是否是合法的，如果合法字符则返回true，否则返回false
     *
     * @param ch 需要判断的字符
     * @return BOOLEAN true: 合法字符 false: 非法字符
     */
    @Override
    public boolean isValidChar(char ch)
    {
        return false;
    }
    
    /**
     * 过滤字符串中的非法字符
     *
     * @param input 需要去除非法字符的字符串
     * @return String 去除非法字符后的字符串
     */
    @Override
    public String stripInvalidChars(String input)
    {
        return null;
    }
}


 