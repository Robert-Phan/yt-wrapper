# yt-wrapper <!-- omit in toc -->
**A simple wrapper around the Youtube Data API.**
***

**Table of contents**
- [Introduction](#introduction)
- [Tutorial/Quickstart](#tutorialquickstart)
- [Guides](#guides)
- [API Reference](#api-reference)
  - [`Client`](#client)
  - [Methods](#methods)
    - [`Playlist`](#playlist)
    - [`PlaylistItem`](#playlistitem)
    - [`Thumbnail`](#thumbnail)
    - [`Comment`](#comment)
    - [`CommentThread`](#commentthread)
    - [`I18n`](#i18n)
    - [`VideoCategory`](#videocategory)
    - [`VideoAbuseReportReason`](#videoabusereportreason)
    - [`Video`](#video)
    - [`Channel`](#channel)
    - [`ChannelSection`](#channelsection)
    - [`Search`](#search)
    - [`Subscription`](#subscription)
  - [Resources](#resources)
    - [`PlaylistResource`](#playlistresource)
    - [`PlaylistItemResource`](#playlistitemresource)
    - [`ThumbnailResource`](#thumbnailresource)
    - [`CommentResource`](#commentresource)
    - [`CommentThreadResource`](#commentthreadresource)
    - [`I18nLanguageResource`](#i18nlanguageresource)
    - [`I18nRegionResource`](#i18nregionresource)
    - [`VideoCategoryResource`](#videocategoryresource)
    - [`VideoAbuseReportReasonResource`](#videoabusereportreasonresource)
    - [`VideoResource`](#videoresource)
    - [`ChannelResource`](#channelresource)
    - [`ChannelSectionResource`](#channelsectionresource)
    - [`SearchResult`](#searchresult)
    - [`SubscriptionResource`](#subscriptionresource)
    - [`PlaylistListResponse`](#playlistlistresponse)
    - [`PlaylistItemListResponse`](#playlistitemlistresponse)
    - [`ThumbnailListResponse`](#thumbnaillistresponse)
    - [`CommentListResponse`](#commentlistresponse)
    - [`CommentThreadListResponse`](#commentthreadlistresponse)
    - [`I18nLanguageListResponse`](#i18nlanguagelistresponse)
    - [`I18nRegionListResponse`](#i18nregionlistresponse)
    - [`VideoCategoryListResponse`](#videocategorylistresponse)
    - [`VideoAbuseReportReasonListResponse`](#videoabusereportreasonlistresponse)
    - [`VideoListResponse`](#videolistresponse)
    - [`ChannelListResponse`](#channellistresponse)
    - [`ChannelSectionListResponse`](#channelsectionlistresponse)
    - [`SearchListResponse`](#searchlistresponse)
    - [`SubscriptionListResponse`](#subscriptionlistresponse)

## Introduction
The goal of this project is to create an (almost) complete, comprehensive Python wrapper for the Youtube Data API. 

**WARNING:** *This project is still unfinished. Breaking changes can be made at any time. Usse at your own risk.*

**NOTE:** This project is my first ever attempt at creating a semi-decent Python package.
## Tutorial/Quickstart 

This section will demonstrate a simple program written using this package. We will be retrieving a video's title with it's ID.

For the full documentation for this package, see the [API Reference](#api-reference).  

1. **Package installation** 
   
    To use this package, you must have `Python 3.10` or higher.

    Install using `pip`:
    ```
    pip install yt-wrapper
    ```
    It is recommended that you use a virtual environment when installing this package.

2. **Authorization**

    *TODO: write the authorizaton process.*

3. **Using the API**
    
    - Setting up the client  

        ```python
        from ytwrapper.client import Client
        youtube = Client.from_client_secrets(path_to_client_secrets_file, scopes=['https://www.googleapis.com/auth/youtube.readonly'])
        ```
    - Getting the video

        ```python
        video = youtube.video.list(
            part='snippet',        # the `snippet` part, which contains the video titles
            id='dQw4w9WgXcQ'       # the Video id of the video we're retrieving
        )

        print(video.snippet.title) # Output: 'Rick Astley - Never Gonna Give You Up (Official Music Video)'
        ```

## Guides

## API Reference

### `Client`
The `Client` class represents a Youtube client, containing the entire API of this project.

**Methods:**
- `from_client_secrets` 
    
    Creates a new `Client` object from an OAuth2 [Installed App](https://developers.google.com/youtube/v3/guides/auth/installed-apps) client secrets file. Will prompt the user to go to a link and give access, where the user will have to copy a code given at the end to the terminal.
    - `client_secrets_file: str`
        
        The path to the client secrets JSON file. This file should contain the client secrets of an [Installed App project.](https://developers.google.com/youtube/v3/guides/auth/installed-apps)
    - `scopes: list[str]`

        [The scope of the program](https://developers.google.com/youtube/v3/guides/auth/installed-apps#identify-access-scopes), specifying the permissions the user must give. Each method in the API has it's own scopes that it needs for it to be used.
    - `token_store: str = "token.pickle"`

        The path to the file used to store the OAuth2 access and refresh token.

**Attributes:**
- `playlist`: The interface for [Playlist](#playlist).
- `playlist_item`: The interface for [PlaylistItem](#playlistitem).
- `thumbnail`: The interface for [Thumbnail](#thumbnail).
- `comment`: The interface for [Comment](#comment).
- `comment_thread`: The interface for [CommentThread](#commentthread).
- `i18n`: The interface for [I18n](#i18n).
- `video_category`: The interface for [VideoCategory](#videocategry).
- `video_abuse_report_reason`: The interface for [VideoAbuseReportReason](#videoabusereportreason).
- `video`: The interface for [Video](#video).
- `channel`: The interface for [Channel](#channel).
- `channel_section`: The interface for [ChannelSection](#channelsection).
- `search`: The interface for [Search](#search).
- `subscription`: The interface for [Subscription](#subscription).

***
### Methods
<!-- TODO: Add in return types for each of these. -->
This section describes the methods available in the API. These methods are accessible via the [`Client`](#client) object.

<!--m-start Playlist -->
#### `Playlist`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a collection of playlists.  
    **Required** parameters:
    - `part: PlaylistPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id: list[str]|str`

        The playlist ID/list of playlist IDs that will be returned.
    - `channel_id: str`

        Specifies a channel ID whose playlists will be returned.
    - `mine: bool`

        Specifies that the API should retrieve the playlists of the authorised user.

    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistListResponse`](#playlistlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Creates a playlist.  
    **Required** parameters:
    - `body: [PlaylistResource](#playlistresource)`

        The [`PlaylistResource`](#playlistresource) which specifies the details of this playlist.  
        **Values you are able to set**:
        - `snippet.title` (Required)
        - `snippet.description`
        - `snippet.privacy_status`
    - `part: PlaylistPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistResource`](#playlistresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a playlist.  
    **Required** parameters:
    - `body: PlaylistResource`

        The [`PlaylistResource`](#playlistresource) which specifies the details of this playlist.  
        **Values you are able to set**:
        - `id` (Required)
        - Otherwise, same as the above `insert` method.`
    - `part: PlaylistPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistResource`](#playlistresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a playlist.  
    **Required** parameters:
    - `playlist_id: str`

        The ID of the playlist that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/delete)
</details>

<!--m-end Playlist -->
<!--m-start PlaylistItem -->
#### `PlaylistItem`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a collection of playlist items that match the API request parameters.  
    **Required** parameters:
    - `part: PlaylistItemPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id: list[str]|str`

        The ID/list of IDs of the playlist items that should be returned.
    - `playlist_id: str`

        The ID of the playlist whose videos will be retrieved.

    **Optional** parameters:
    - `video_id: str`

        Specifies that the request should return only the playlist items that contain the specified video.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistItemListResponse`](#playlistitemlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/playliststems/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Modifies a playlist item.  
    **Required** parameters:
    - `body: PlaylistItemResource`

        The [`PlaylistItemResource`](#playlistitemresource) which specifies the details of the playlist item.  
        **Values you are able to set**:
        - `snippet.playlist_id` (Required)
        - `snippet.resource_id` (Required)
        - `snippet.position`
        - `content_details.note`
        - `content_details.start_at`
        - `content_details.end_at`
    - `part: PlaylistItemPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistItemResource`](#playlistitemresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Inserts a video into a playlist.  
    **Required** parameters:
    - `body: PlaylistItemResource`

        The [`PlaylistItemResource`](#playlistitemresource) which specifies the details of the playlist item.  
        **Values you are able to set**:
        - `id` (Required)
        - Otherwise, same as the above `insert` method.`
    - `part: PlaylistItemPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistItemResource`](#playlistitemresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a playlist item.  
    **Required** parameters:
    - `playlist_item_id: str`

        The ID of the playlist item that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/delete)
</details>

<!--m-end PlaylistItem -->
<!--m-start Thumbnail -->
#### `Thumbnail`
**Methods:**
- <details><summary><code>set</code></summary>
    <br>

    Uploads a custom video thumbnail to YouTube and sets it for a video.  
    **Required** parameters:
    - `thumbnail_file: str`

        The path to the file of the thumbnail.
    - `video_id: str`

        The ID of the video for the thumbnail.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ThumbnailListResponse`](#thumbnaillistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/thumbnails/set)
</details>

<!--m-end Thumbnail -->
<!--m-start Comment -->
#### `Comment`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of comments.  
    **Required** parameters:
    - `part: CommentPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id`

        The id of the comment that should be retrived.
    - `parent_id`

        The ID of the top-level comment whose replies should be retrieved.

    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `text_format: Literal['html', 'plain_text']`

        The format of the returned comment.

    **Returns:** [`CommentListResponse`](#commentlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/comments/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Create a reply to a top-level comment. To create a top-level comment, use CommentThread.insert instead.  
    **Required** parameters:
    - `body: CommentResource`

        The [`CommentResource`](#commentresource) which specifies the details of the reply.  
        **Values you are able to set**:
        - `snippet.text_original`
        - `snippet.parent_id`
    - `part: CommentPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`CommentResource`](#commentresource)

    [Reference](https://developers.google.com/youtube/v3/docs/comments/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Modifies a comment.  
    **Required** parameters:
    - `body: CommentResource`

        The [`CommentResource`](#commentresource) which specifies the details of the comment.  
        **Values you are able to set**:
        - `id`(Required)
        - `snippet.text_original`
    - `part: CommentPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`CommentResource`](#commentresource)

    [Reference](https://developers.google.com/youtube/v3/docs/comments/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a comment.  
    **Required** parameters:
    - `comment_id: str`

        The ID of the comment that should be deleted.

    [Reference](https://developers.google.com/youtube/v3/docs/comments/delete)
</details>

<!--m-end Comment -->
<!--m-start CommentThread -->
#### `CommentThread`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of comment threads.  
    **Required** parameters:
    - `part: CommentThreadPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id: str`

        The ID of the comment.
    - `channel_id: str`

        Specifies the API to retrieve all comment threads which contain comments from this channel.
    - `video_id: str`

        Specifies the ID of the video whose comments should be retrieved.
    - `all_threads_related_to_channel_id: str`

        Specifies the API to return all comment threads associated with the specified channel.

    **Optional** parameters:
    - `moderation_status: Literal['held_for_review', 'likely_spam', 'published']`

        Specifies that all returned comments are of the given moderation state.
    - `order: Literal['time', 'relevance']`

        Specifies the order the returned comment threads should be in.
    - `text_format: Literal['html', 'plain_text']`

        The format of the returned comment.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`CommentThreadListResponse`](#commentthreadlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/commentThreads/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Create a new top-level comment.  
    **Required** parameters:
    - `body: CommentThreadResource`

        The [`CommentThreadResource`](#commentthreadresource) which specifies the details of the comment.  
        **Values you are able to set**:
        - `snippet.channel_id`
        - `snippet.video_id`
        - `snippet.top_level_comment.snippet.text_original`
    - `part: CommentThreadPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`CommentThreadResource`](#commentthreadresource)

    [Reference](https://developers.google.com/youtube/v3/docs/commentThreads/insert)
</details>

<!--m-end CommentThread -->
<!--m-start I18n -->
#### `I18n`
**Methods:**
- <details><summary><code>list_languages</code></summary>
    <br>

    Returns a list of languages that YouTube supports.  
    **Returns:** [`I18nLanguageListResponse`](#i18nlanguagelistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/i18nLanguages/list/)
</details>

- <details><summary><code>list_regions</code></summary>
    <br>

    Returns a list of content regions that YouTube supports.  
    **Returns:** [`I18nLanguageRegionResponse`](#i18nlanguageregionresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/i18nRegions/list/)
</details>

<!--m-end I18n -->
<!--m-start VideoCategory -->
#### `VideoCategory`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a list of categories that can be associated with YouTube videos.  
    **Optional** parameters:
    - `id: str|list[str]`

        The ID of the video category to be retrieved.
    - `region_code: str`

        Specifies the API to retrive all video categories in the specified region code.

    **Returns:** [`VideoCategoryListResponse`](#videocategorylistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/videoCategories/list)
</details>

<!--m-end VideoCategory -->
<!--m-start VideoAbuseReportReason -->
#### `VideoAbuseReportReason`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of reasons that can be used to report abusive videos.  
    **Returns:** [`VideoAbuseReportReasonListResponse`](#videoabusereportreasonlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list)
</details>

<!--m-end VideoAbuseReportReason -->
<!--m-start Video -->
#### `Video`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieves a list of videos.  
    **Required** parameters:
    - `part: VideoPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `chart: Literal['most_popular']`

        Identifies the chart that you want to retrieve.
    - `id: list[str]|str`

        Specifies the video(s) that should be retrieved.
    - `my_rating: Literal["like", "dislike"]`

        Specifies that the API should only retrieve videos that the user has disliked/like.

    **Optional** parameters:
    - `region_code: str`

        Specifies the API to select a video chart in the specified region code.
        Used in conjunction with the `chart` parameter.
    - `video_category_id: str`

        Specifies the video category for which the chart should be retrieved.
        Used in conjunction with the `chart` parameter.
    - `max_height: int`

        Specifies the maximum height of the embedded player returned in the `player.embed_html` property
    - `max_width: int`

        Specifies the maximum width of the embedded player returned in the `player.embed_html` property
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoListResponse`](#videolistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Upload a video to youtube.  
    **Required** parameters:
    - `body: VideoResource`

        The [`VideoResource`](#videoresource) which specifies the details of the comment.  
        **Values you are able to set**:
        - `snippet.title`
        - `snippet.description`
        - `snippet.tags`
        - `snippet.category_id`
        - `snippet.default_language`
        - `status.embeddable`
        - `status.license`
        - `status.public_stats_viewable`
        - `status.publish_at`
        - `status.self_declared_made_for_kids`
        - `recording_details.recording_date`
    - `part: VideoPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `media_body: str`

        The path to the file of the uploaded video.

    **Optional** parameters:
    - `notify_subscribers: bool`

        Indicates whether YouTube should notify subscribers to the video's channel about the video.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoResource`](#videoresource)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a video's metadata.  
    **Required** parameters:
    - `body: VideoResource`

        The [`VideoResource`](#videoresource) which specifies the details of the video.  
        **Values you are able to set**:
        - `id` (Required)
        - `snippet.title (Required IF updating the `snippet` attribute.)`
        - `snippet.description`
        - `snippet.tags`
        - `snippet.category_id`
        - `snippet.default_language`
        - `status.embeddable`
        - `status.license`
        - `status.public_stats_viewable`
        - `status.publish_at`
        - `status.self_declared_made_for_kids`
        - `recording_details.recording_date`
    - `part: VideoPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoResource`](#videoresource)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a video.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/videos/delete)
</details>

- <details><summary><code>rate</code></summary>
    <br>

    Rate a video.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video to rate.
    - `rating: Literal['dislike', 'like', 'none']`

        The rating to give to the video.

    [Reference](https://developers.google.com/youtube/v3/docs/videos/rate)
</details>

- <details><summary><code>get_rating</code></summary>
    <br>

    Get a video's rating.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video whose rating shall be retrieved.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoGetRatingResponse`](#videogetratingresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/getrating)
</details>

<!--m-end Video -->
<!--m-start Channel -->
#### `Channel`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a channel/list of channel resources.  
    **Required** parameters:
    - `part: ChannelPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `mine: bool`

        Specifies that the API should retrieve the channel of the authorised user.
    - `for_username: str`

        Specifies the name of the channel that should retrieve.
    - `id: str|list[str]`

        The ID of the channel to be retrieved.
    - `managed_by_me: bool`

        Specifies that the API should retrieve channels managed by the authenticated user.

    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelListResponse`](#channellistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/channels/list)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a channel.  
    **Required** parameters:
    - `body: ChannelResource`

        The [`ChannelResource`](#channelresource) which specifies the details of the channel.  
        **Values you are able to set**:
        - `branding_settings.channel.description`
        - `branding_settings.channel.country`
        - `branding_settings.channel.default_language`
        - `branding_settings.channel.keywords`
        - `branding_settings.channel.moderate_comments`
        - `branding_settings.channel.tracking_analytics_account_id`
        - `branding_settings.channel.unsubscribed_trailer`
        - `status.self_declared_made_for_kids`
    - `part: ChannelPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelResource`](#channelresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channels/update)
</details>

<!--m-end Channel -->
<!--m-start ChannelSection -->
#### `ChannelSection`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of channel sections.  
    **Required** parameters:
    - `part: ChannelSectionPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `channel_id: str`

        Specifies a channel ID whose channel sections will be returned.
    - `id: str`

        The ID of the sections that should be retrieved.
    - `mine: bool`

        Specifies that the API should retrieve the channel section of the authorised user.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelSectionListResponse`](#channelsectionlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Adds a channel section to the autheticated user's channel.  
    **Required** parameters:
    - `body: ChannelResource`

        The [`ChannelSectionResource`](#channelsectionresource) which specifies the details of the channel.  
        **Values you are able to set**:
        - `id`
        - `snippet.type`
        - `snippet.title`
        - `snippet.position`
        - `content_details.playlists`
        - `content_details.channels`
    - `part: ChannelSectionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.
    - `on_behalf_of_content_owner_channel: str`

        Specifies the YouTube channel ID of the channel to which a video is being added.

    **Returns:** [`ChannelSectionResource`](#channelsectionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a channel section.  
    **Required** parameters:
    - `body: ChannelResource`

        The [`ChannelSectionResource`](#channelsectionresource) which specifies the details of the channel.  
        **Values you are able to set**:
        - `id`
        - `snippet.type`
        - `snippet.title`
        - `snippet.position`
        - `content_details.playlists`
        - `content_details.channels`
    - `part: ChannelSectionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelSectionResource`](#channelsectionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a channel section.  
    **Required** parameters:
    - `section_id: str`

        The ID of the channel section that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/delete)
</details>

<!--m-end ChannelSection -->
<!--m-start Search -->
#### `Search`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Searches something on youtube.  
    **Required** parameters:
    - `q: str`

        The query to search for.

    **Filters** (specify one or zero of these parameters.):
    - `for_content_owner: bool`

        Restricts the search to only retrieve videos owned by the content owner identified by the `on_behalf_of_content_owner` parameter.
    - `for_developer: bool`

        Restricts the search to only retrieve videos uploaded via the developer's application or website.
    - `for_mine: bool`

        Restricts the search to only retrieve videos owned by the authenticated user.
    - `related_to_video_id: bool`

        Specifies the ID of a video. The API will restrict the search result to videos related to that video.

    **Optional** parameters:
    - `order: Literal['date', 'rating', 'relevance', 'title', 'videoCount', 'viewCount']`

        Specifies the order of the resource.
    - `safe_search: Literal['none', 'moderate', 'strict']`

        Specifies whether the API should retrieve restricted content or not.
    - `type: Literal['channel', 'playlist', 'video']`

        Specifies what type of resource will be returned.
    - `published_after: str`

        Restricts the API to only return resources published after the specified time in the parameter.
    - `published_before: str`

        Restricts the API to only return resources published before the specified time in the parameter.
    - `region_code: str`

        Specifies to return search results available in the region code.
    - `relevance_language: str`

        Specifies to return search results that are most relevant to the specified language.
    - `location: str`

        Restricts the search result to resources published in the specified location.
        Used in conjunction with `location_radius`.
    - `location_radius: str`

        Specifies the area around the point provided by `location` to restrict videos.
    - `channel_id: str`

        Specifies that the result should only contain resources published by the provided channel.
    - `channel_type: Literal['show']`

        Restricts the search to a particular type of channel.
    - `event_type: Literal['completed', 'live', 'upcoming']`

        Restricts a search to broadcast events.
        Set the `type` parameter to `video` when specifying this parameter.
    - `video_caption: Literal['closedCaption', 'none']`

        See the attached reference.
    - `video_category_id: str`

        See the attached reference.
    - `video_definition: Literal['high', 'standard']`

        See the attached reference.
    - `video_dimension: Literal['2d', '3d']`

        See the attached reference.
    - `video_duration: Literal['long', 'medium', 'short']`

        See the attached reference.
    - `video_embeddable: Literal['true']`

        See the attached reference.
    - `video_license: Literal['creativeCommon', 'youtube']`

        See the attached reference.
    - `video_syndicated: Literal['true']`

        See the attached reference.
    - `video_type: Literal['episode', 'movie']`

        See the attached reference.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`SearchResultListResponse`](#searchresultlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/search/list)
</details>

<!--m-end Search -->
<!--m-start Subscription -->
#### `Subscription`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve subscription resources.  
    **Required** parameters:
    - `part: SubscriptionPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `channel_id: str`

        Specifies a channel ID whose subscriptions will be returned.
    - `id: str|list[str]`

        The ID of the channel to be retrieved.
    - `mine: bool`

        Specifies that the API should retrieve the subscriptions of the authorised user.
    - `my_recent_subscribers: bool`

        Retrieve a feed of the subscribers of the authenticated user in reverse chronological order.
    - `my_subscribers: bool`

        Retrieve a feed of the subscribers of the authenticated user in no particular order

    **Optional** parameters:
    - `order: Literal['alphabetical', 'relevance', 'unread']`

        Specifies the method that will be used to sort resources in the response.
    - `for_channel_id: str`

        Specifies a list of channel IDs, which the APi will only match to.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.
    - `on_behalf_of_content_owner_channel: str`

        Specifies the YouTube channel ID of the channel to which a video is being added.

    **Returns:** [`SubscriptionListResponse`](#subscriptionlistresponse)

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Subscribe to a channel.  
    **Required** parameters:
    - `channel_id: str`

        Specifies a channel ID to subscribe to.
    - `part: SubscriptionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`SubscriptionResource`](#subscriptionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/insert)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a subscription.  
    **Required** parameters:
    - `subscription_id: str`

        The ID of the subscription that will be deleted.

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/delete)
</details>

<!--m-end Subscription -->

***
### Resources
This section describes the resources and responses used in the API. These classes are most often used in responses, as well as in methods that require a request body.  
Note that the attributes of these resources are in `snake_case`, not `camelCase` like in the original response. This is so as to follow the Python conventions.  
Also note that each resource has a `to_dict` method that returns the original response. That original response is a Python dictionary, and it's keys *will* be in `camelCase`. 

<!--r-start PlaylistResource -->
#### `PlaylistResource`
Represents a Youtube playlist.
- <details><summary><code>PlaylistResource</code></summary>
    
    - `kind`
    
        Identifies the API resource's type.
    - `etag: str`
    
        The etag of the resource.
    - `id: str`
    
        The ID of the playlist.
    - `snippet`
    
        Basic details about the playlist.
        - `published_at: str`
    
            The date when this was published at.
        - `channel_id: str`
    
            The ID of the channel which published the playlist.
        - `title: str`
    
            The title of the playlist.
        - `description: str`
    
            The description of the playlist
        - `thumbnails: ThumbnailResource`
    
            The thumbnails of the playlist.
        - `channel_title: str`
    
            The title of the channel which published the playlist.
        - `default_language: str`
    
            The language of the text in the `snippet.title` and `snippet.description` attributes.
        - `localized`
    
            Localized title and description.
            - `title: str`
    
                Localized title.
            - `description: str`
    
                Localized description.
    - `status`
    
        Status information of the playlist.
        - `privacy_status: str`
    
            The playlist's privacy status.
    - `content_details`
    
        Information about the playlist's content.
        - `item_count: int`
    
            The number of videos in the playlist.
    - `player`
    
        Information about the playlist in an embedded player.
        - `embed_html: str`
    
            An `<iframe>` tag that embeds a player 
</details>
<!--r-end PlaylistResource -->

<!--r-start PlaylistItemResource -->
#### `PlaylistItemResource`
Represents a video in a playlist.
- <details><summary><code>PlaylistItemResource</code></summary>
    
    - `kind`
    
        Identifies the API resource's type.
    - `etag: str`
    
        The etag of the resource.
    - `id: str`
    
        The ID of the playlist item.
    - `snippet`
    
        Basic details about the playlist item.
        - `published_at: str`
    
            The date when this was published at.
        - `channel_id: str`
    
            The ID of the channel which added the item to the playlist..
        - `title: str`
    
            The title of the playlist item.
        - `description: str`
    
            The description of the playlist item.
        - `thumbnails: ThumbnailResource`
    
            The thumbnails of the playlist item.
        - `channel_title: str`
    
            The title of the channel which added the video.
        - `video_owner_channel_title: str`
    
            The title of the channel that the video belonged to.
        - `video_owner_channel_id: str`
    
            The id of the channel that the video belonged to.
        - `playlist_id: str`
    
            The ID of the playlist that the resource belonged to.
        - `position: int`
    
            The order of the item in the playlist.
        - `resourceId`
    
            Contains info that identifies the resource.
            - `kind: str`
    
                The kind/type of the resource.
            - `video_id: str`
    
                The ID of the video.
    - `content_details`
    
        Additional info about the video.
        - `video_id: str`
    
            The ID of the video.
        - `note: str`
    
            The user generated note for this item.
        - `video_published_at: str`
    
            The time the video was published at.
    - `status`
    
        Info about the playlist item's privacy status.
        - `privacy_status: str`
    
            The playlist item's privacy status.
</details>
<!--r-end PlaylistItemResource -->

<!--r-start ThumbnailResource -->
#### `ThumbnailResource`
Identifies different thumbnail image sizes associated with a resource.
- <details><summary><code>ThumbnailResource</code></summary>
    
    - `default`
    
        The default thumbnail image. 120px wide and 90px tall for a video, 88px wide and 88px tall for a channel.
        - `url: str`
    
            The image's URL.
        - `width: int`
    
            The image's width.
        - `height: int`
    
            The image's height.
    - `medium`
    
        A higher resolution version of the thumbnail. 320px wide and 180px tall for a video, 240px wide and 240px for a channel.
        - `url: str`
    
            The image's URL.
        - `width: int`
    
            The image's width.
        - `height: int`
    
            The image's height.
    - `high`
    
        A high resolution version of the thumbnail. 480px wide and 360px tall for a video, 800px wide and 800px for a channel.
        - `url: str`
    
            The image's URL.
        - `width: int`
    
            The image's width.
        - `height: int`
    
            The image's height.
    - `standard`
    
        An even higher resolution version of the thumbnail. 640px wide and 480px tall for a video.
        - `url: str`
    
            The image's URL.
        - `width: int`
    
            The image's width.
        - `height: int`
    
            The image's height.
    - `maxres`
    
        The highest resolution version of the thumbnail image. 1280px wide and 720px tall for a video.
        - `url: str`
    
            The image's URL.
        - `width: int`
    
            The image's width.
        - `height: int`
    
            The image's height.
</details>
<!--r-end ThumbnailResource -->

<!--r-start CommentResource -->
#### `CommentResource`
Represents a single Youtube comment.
- <details><summary><code>CommentResource</code></summary>
    
    - `kind: str`
    
        The kind/type of the resource.
    - `etag: str`
    
        The etag of the resource.
    - `id: str`
    
        The ID of the comment.
    - `snippet`
    
        Basic details about the comment.
        - `author_display_name: str`
    
            The name of the commenter.
        - `author_profile_image_url: str`
    
            The URL to the profile image of the commenter.
        - `author_channel_url: str`
    
            The URL of the commenter's channel.
        - `author_channel_id`
    
            Info about the author's channel
            - `value: str`
    
                The author's channel ID.
        - `channel_id: str`
    
            The channel ID who uploaded the video the comment was left on.
        - `video_id: str`
    
            The ID of the video the comment was left on.
        - `text_display: str`
    
            The comment's text, either in plain text or HTML form.
        - `text_original: str`
    
            The original, unedited comment text.
        - `parent_id: str`
    
            The ID of the comment's parent (if the comment is a reply).
        - `can_rate: bool`
    
            Whether the authorised user is able to rate the comment.
        - `viewer_rating: str`
    
            The rating the authorised user gave to the comment.
        - `like_count: int`
    
            The like count of the comment.
        - `moderation_status: str`
    
            The comment's moderation status.
        - `published_at: str`
    
            The date and time when the comment was orignally published.
        - `updated_at: str`
    
            The date and time when the comment was last updated.
</details>
<!--r-end CommentResource -->

<!--r-start CommentThreadResource -->
#### `CommentThreadResource`
Represents a Youtube comment thread, consisting of a top-level comment and it's replies.
- <details><summary><code>CommentThreadResource</code></summary>
    
    - `kind: str`
    
        The kind/type of the resource.
    - `etag: str`
    
        The etag of the resource.
    - `id: str`
    
        The ID of the comment thread.
    - `snippet`
    
        Basic details about the comment thread.
        - `channel_id: str`
    
            The Youtube channel associated with the comment thread.
        - `video_id: str`
    
            The video that the comment thread is under/
        - `top_level_comment: CommentResource`
    
            The top-level comment.
        - `can_reply: bool`
    
            Whether the authorised user can reply to the comment thread or not.
        - `total_reply_count: int`
    
            The amount of replies in the comment thread.
        - `is_public: bool`
    
            Whether the comment thread is public or not.
    - `replies`
    
        A container of the comment thread's replies. `replies.comments` represents the list of replies themselves.
        - `comments: list[CommentResource]`
    
            A list containing the replies. Only a subset of replies will be available in the this list. To get the full amount of replies from a comment thread, use the `comment.list` method.
</details>
<!--r-end CommentThreadResource -->

<!--r-start I18nLanguageResource -->
#### `I18nLanguageResource`
Identifies a language that Youtube supports.
- <details><summary><code>I18nLanguageResource</code></summary>
    
    - `kind: str`
    
        The kind/type of the resource.
    - `etag: str`
    
        The etag of the resource.
    - `id: str`
    
        The ID of the I18n language.
    - `snippet`
    
        Basic details about the language.
        - `hl: str`
    
            A BCP-47 code that uniquely identifies a language.
        - `name: str`
    
            The name of the language.
</details>
<!--r-end I18nLanguageResource -->

<!--r-start I18nRegionResource -->
#### `I18nRegionResource`
Identifies a region that Youtube supports.
- <details><summary><code>I18nRegionResource</code></summary>
    
    - `kind: str`
    
        The kind/type of the resource.
    - `etag: str`
    
        The etag of the resource.
    - `id: str`
    
        The ID of the I18n region.
    - `snippet`
    
        Basic details about the region.
        - `gl: str`
    
            The two-letter ISO country code that identifies a language.
        - `name: str`
    
            The name of the region.
</details>
<!--r-end I18nRegionResource -->

<!--r-start VideoCategoryResource -->
#### `VideoCategoryResource`
Identifies a category associated with a Youtube video.
- <details><summary><code>VideoCategoryResource</code></summary>
    
    - `kind: str`
    
        The kind/type of the resource.
    - `etag: str`
    
        The etag of the resource.
    - `id: str`
    
        The ID of the category.
    - `snippet`
    
        Basic details about the category.
        - `channel_id: str`
    
            The channel that created the category, which is Youtube itself. The value will be `UCBR8-60-B28hp2BmDPdntcQ`
        - `title: str`
    
            The title of the category.
        - `assignable: bool`
    
             Indicates whether videos can be associated with the category.
</details>
<!--r-end VideoCategoryResource -->

<!--r-start VideoAbuseReportReasonResource -->
#### `VideoAbuseReportReasonResource`
Contains information about a reason that a video could be reported for.
- <details><summary><code>VideoAbuseReportReasonResource</code></summary>
    
    - `kind: str`
    
        The kind/type of the resource.
    - `etag: str`
    
        The etag of the resource.
    - `id: str`
    
        The ID of the reason.
    - `snippet`
    
        Basic details about the reason.
        - `label: str`
    
            The localized label text for the reason.
        - `secondary_reasons: list`
    
            A list of secondary reasons associated with the reason.
            - `id: str`
    
                The ID of the secondary reason.
            - `label: str`
    
                The localized label text for the reason. 
</details>
<!--r-end VideoAbuseReportReasonResource -->

<!--r-start VideoResource -->
#### `VideoResource`
Represents a Youtube video.
- <details><summary><code>VideoResource</code></summary>
    
    - `kind`
    
        youtube#video
    - `etag`
    
        etag
    - `id: str`
    
        The ID of the video.
    - `snippet`
    
        Basic details about the video.
        - `published_at: str`
    
            The date and time when the video was published.
        - `channel_id: str`
    
            The ID of the channel that uploaded the video.
        - `title: str`
    
            The title of the video.
        - `description: str`
    
            The description of the video
        - `thumbnails: ThumbnailResource`
    
            The thumbnails of the video.
        - `channel_title: str`
    
            The title of the video's uploader.
        - `tags: list[str]`
    
            The tags associated with the video.
        - `category_id: str`
    
            The ID of the category the video belongs to.
        - `live_broadcast_content: str`
    
            Indicates if the video is an upcoming/active live broadcast.
        - `default_language: str`
    
            The language of the text in the `snippet.title` and `snippet.description` attributes.
        - `localized`
    
            Contains the localized title and description for the video.s
            - `title: str`
    
                The localized video title.
            - `description: str`
    
                 The localized video description.
    - `content_details`
    
        Contains information about the video content.
        - `duration: str`
    
            The length of the video.
        - `dimension: str`
    
            Indicates whether the video is 2D or 3D
        - `definition: str`
    
            Indicates whether the video is in HD or just SD.
        - `caption: str`
    
            Indicates whether the video has captions or not.
        - `licensed_content: bool`
    
            Indicates whether the video represents licensed content.
        - `region_restriction`
    
            Contains info about which regions the video is viewable.
            - `allowed: list[str]`
    
                A list of region codes that identify countries where the video is viewable.
            - `blocked: list[str]`
    
                A list of region codes that identify countries where the video is blocked.
        - `content_rating`
    
            Specifies the video's rating under various rating schemes.
        - `projection: str`
    
            Specifies whether the video's projection is `360` or `rectangular`.
        - `has_custom_thumbnail: bool`
    
            Whether the video has a custom thumbnail or not.
    - `status`
    
        Contains information about the video's uploading, processing, and privacy statuses.
        - `upload_status: str`
    
            The status of the uploaded video.
        - `failure_reason: str`
    
            Explains why a video failed to upload. Available when `upload_status` identifies that the video failed to upload.
        - `rejection_reason: str`
    
            Explains why the uploaded video got rejected. Available when `upload_status` identifies that the video was rejected.
        - `privacy_status: str`
    
            The video's privacy status.
        - `publish_at: str`
    
            The date and time when the video is scheduled to publish.
        - `license: str`
    
             The video's license.
        - `embeddable: bool`
    
            Whether the video can be embedded on another website.
        - `public_stats_viewable: bool`
    
            Whether the extended statistics on the video's watch page are publicly viewable.
        - `made_for_kids: bool`
    
            Whether the video is designated as made for kids.
        - `self_declared_made_for_kids: bool`
    
            Whether the video is designated by the creator as made for kids.
    - `statistics`
    
        Contains statistics about the video.
        - `view_count: int`
    
            The amount of views the video has.
        - `like_count: int`
    
            The amount of likes the video has.
        - `dislike_count: int`
    
            The amount of dislikes the video has. Only available if the user is the video uploader.
        - `favorite_count: int`
    
            <font color='red'>Deprecated.</font>
        - `comment_count: int`
    
            The amount of comments the video has.
    - `player`
    
        Information about the video in an embedded player.
        - `embed_html: str`
    
            An `<iframe>` which embeds a player that plays the video.
        - `embed_height: int`
    
            The height of the player.
        - `embed_width: int`
    
            The width of the player.
    - `topic_details`
    
        Contains info about the topics associated with the video.
        - `topic_ids: list[str]`
    
            <font color='red'>Deprecated.</font>
        - `relevantTopic_ids: list[str]`
    
            A list of topic IDs that are relevant to the video.
        - `topic_categories: list[str]`
    
            A list of Wikipedia URLs that provide a high-level description of the video's content.
    - `recordingDetails`
    
        Contains info about the recording.
        - `recording_date: str`
    
            When the video was recorded.
    - `file_details`
    
        Contains info about the file that was uploaded to Youtube.
        - `file_name: str`
    
            The name of the file.
        - `file_size: int`
    
            The size of the file in bytes.
        - `file_type: str`
    
            The type of the file.
        - `container: str`
    
            The container format of the file.
        - `duration_ms: int`
    
            The length of the video in milliseconds.
        - `bitrate_bps: int`
    
            The video's bitrate in bits per seconds.
        - `creation_time: str`
    
            When the video is created, in ISO 8601 format.
        - `video_streams: list`
    
            A list of video streams contained in the uploaded video file.
            - `width_pixels: int`
    
                The encoded video content's width in pixels.
            - `height_pixels: int`
    
                The encoded video content's height in pixels
            - `frame_rate_fps: int`
    
                The video stream's frame rate, in frames per second.
            - `aspect_ratio: int`
    
                The video content's display aspect ratio.
            - `codec: str`
    
                The video codec that the stream uses.
            - `bitrate_bps: int`
    
                 The video stream's bitrate, in bits per second.
            - `rotation: str`
    
                The amount that YouTube needs to rotate the original source content to properly display the video.
            - `vendor: str`
    
                A value (usually a four-letter code) that uniquely identifies a video vendor.
        - `audio_streams: list`
    
            A list of audio streams contained in the uploaded video file.
            - `channel_count: int`
    
                The number of audio channels that the stream contains.
            - `codec: str`
    
                 The audio codec that the stream uses.
            - `bitrate_bps: int`
    
                 The audio stream's bitrate, in bits per second.
            - `vendor: str`
    
                A value (usually a four-letter code) that uniquely identifies a video vendor.
    - `processing_details`
    
        Contains information about YouTube's progress in processing the uploaded video file.
        - `processing_status: str`
    
            The video's processing status.
        - `processing_progress`
    
            Contains information about the progress YouTube has made in processing the video.
            - `parts_total: int`
    
                An estimate of the total number of parts that need to be processed for the video.
            - `parts_processed: int`
    
                The number of parts of the video that YouTube has already processed.
            - `time_left_ms: int`
    
                 An estimate of the amount of time, in millseconds, that YouTube needs to finish processing the video.
        - `processing_failure_reason: str`
    
            The reason that YouTube failed to process the video.
        - `file_details_availability: str`
    
            Whether file details are available for the uploaded video.
        - `processing_issues_availability: str`
    
            Whether the processor has generated suggestions and warnings that explains processing issues.
        - `tag_suggestions_availability: str`
    
            Indicates whether keyword (tag) suggestions are available for the video.
        - `editor_suggestions_availability: str`
    
            Whether video editing suggestions are available for the video.
        - `thumbnails_availability: str`
    
            Whether thumbnail images have been generated for the video.
    - `suggestions`
    
        Encapsulates suggestions that identify opportunities to improve the video quality or the metadata for the uploaded video.
        - `processing_errors: list[str]`
    
            A list of errors that will prevent YouTube from successfully processing the uploaded video.
        - `processing_warnings: list[str]`
    
            A list of reasons why YouTube may have difficulty transcoding the uploaded video.
        - `processing_hints: list[str]`
    
            A list of suggestions that may improve YouTube's ability to process the video.
        - `editor_suggestions: list[str]`
    
            A list of video editing operations that might improve the video quality or playback experience of the uploaded video.
        - `tag_suggestions: list`
    
            A list of keyword tags that could be added to the video's metadata to increase the likelihood that users will locate your video when searching or browsing on YouTube.
            - `tag: str`
    
                The keyword tag suggested for the video.
            - `category_restricts: list[str]`
    
                A set of video categories for which the tag is relevant.
    - `live_streaming_details`
    
        Contains metadata about a live video broadcast.
        - `actual_start_time: str`
    
            The time the broadcast started.
        - `actual_end_time: str`
    
            The time the broadcast ended.
        - `scheduled_start_time: str`
    
            The time the broadcast was scheduled to start.
        - `scheduled_end_time: str`
    
            The time the broadcast was scheduled to end.
        - `concurrent_viewers: int`
    
            The amount of viewers currently watching the stream.
        - `active_live_chat_id: str`
    
            The ID of the currently active live chat attached to this video.
</details>
<!--r-end VideoResource -->

<!--r-start ChannelResource -->
#### `ChannelResource`

- <details><summary><code>ChannelResource</code></summary>

</details>
<!--r-end ChannelResource -->

<!--r-start ChannelSectionResource -->
#### `ChannelSectionResource`

- <details><summary><code>ChannelSectionResource</code></summary>

</details>
<!--r-end ChannelSectionResource -->

<!--r-start SearchResult -->
#### `SearchResult`

- <details><summary><code>SearchResult</code></summary>

</details>
<!--r-end SearchResult -->

<!--r-start SubscriptionResource -->
#### `SubscriptionResource`

- <details><summary><code>SubscriptionResource</code></summary>

</details>
<!--r-end SubscriptionResource -->

<!--r-start PlaylistListResponse -->
#### `PlaylistListResponse`

- <details><summary><code>PlaylistListResponse</code></summary>

</details>
<!--r-end PlaylistListResponse -->  

<!--r-start PlaylistItemListResponse -->
#### `PlaylistItemListResponse`

- <details><summary><code>PlaylistItemListResponse</code></summary>

</details>
<!--r-end PlaylistItemListResponse -->  

<!--r-start ThumbnailListResponse -->
#### `ThumbnailListResponse`

- <details><summary><code>ThumbnailListResponse</code></summary>

</details>
<!--r-end ThumbnailListResponse -->  

<!--r-start CommentListResponse -->
#### `CommentListResponse`

- <details><summary><code>CommentListResponse</code></summary>

</details>
<!--r-end CommentListResponse -->  

<!--r-start CommentThreadListResponse -->
#### `CommentThreadListResponse`

- <details><summary><code>CommentThreadListResponse</code></summary>

</details>
<!--r-end CommentThreadListResponse -->  

<!--r-start I18nLanguageListResponse -->
#### `I18nLanguageListResponse`

- <details><summary><code>I18nLanguageListResponse</code></summary>

</details>
<!--r-end I18nLanguageListResponse -->  

<!--r-start I18nRegionListResponse -->
#### `I18nRegionListResponse`

- <details><summary><code>I18nRegionListResponse</code></summary>

</details>
<!--r-end I18nRegionListResponse -->  

<!--r-start VideoCategoryListResponse -->
#### `VideoCategoryListResponse`

- <details><summary><code>VideoCategoryListResponse</code></summary>

</details>
<!--r-end VideoCategoryListResponse -->  

<!--r-start VideoAbuseReportReasonListResponse -->
#### `VideoAbuseReportReasonListResponse`

- <details><summary><code>VideoAbuseReportReasonListResponse</code></summary>

</details>
<!--r-end VideoAbuseReportReasonListResponse -->  

<!--r-start VideoListResponse -->
#### `VideoListResponse`

- <details><summary><code>VideoListResponse</code></summary>

</details>
<!--r-end VideoListResponse -->  

<!--r-start ChannelListResponse -->
#### `ChannelListResponse`

- <details><summary><code>ChannelListResponse</code></summary>

</details>
<!--r-end ChannelListResponse -->  

<!--r-start ChannelSectionListResponse -->
#### `ChannelSectionListResponse`

- <details><summary><code>ChannelSectionListResponse</code></summary>

</details>
<!--r-end ChannelSectionListResponse -->  

<!--r-start SearchListResponse -->
#### `SearchListResponse`

- <details><summary><code>SearchListResponse</code></summary>

</details>
<!--r-end SearchListResponse -->  

<!--r-start SubscriptionListResponse -->
#### `SubscriptionListResponse`

- <details><summary><code>SubscriptionListResponse</code></summary>

</details>
<!--r-end SubscriptionListResponse -->  
